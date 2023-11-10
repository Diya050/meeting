# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappé and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator
from datetime import datetime,date
from frappe.utils import get_time


class Meeting(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/meeting.html"
	)

	def validate(self):
		self.page_name = self.name.lower()
		self.validate_attendees()
		self.validate_time()
		self.check_for_conflicting_meetings()

		# Check if a title is provided
		if not self.title:
			frappe.throw("Meeting title is required.")
        
		# Set the title as the name if the name is not provided
		if not self.name:
			self.name = self.title
			
        
		# Check if a meeting with the same name already exists
		existing_meetings = frappe.get_all("Meeting",
			filters={"name": self.name},
			fields=["name"],
			limit=1
		)
		
		if existing_meetings:
			# Automatically generate a unique name based on the title
			self.name, self.title = self.get_unique_name(self.name)



	def get_unique_name(self, title):
		# Get the base name from the title
		base_name = title.replace(' ', '_')
		# Find a unique name by appending a counter
		counter = 1
		unique_name = base_name

		while frappe.get_all("Meeting", filters={"name": unique_name}):
			counter += 1
			unique_name = f"{base_name.title()} No. {counter}"
		updated_title = unique_name.replace('-', ' ')

		return unique_name, updated_title
	
	def before_save(self):
		# Calculate the duration if both from_time and to_time are set
		if self.from_time and self.to_time:
			self.from_time = str(self.from_time)  # Convert to string
			self.to_time = str(self.to_time) 
			from_time = datetime.strptime(self.from_time, "%H:%M:%S")
			to_time = datetime.strptime(self.to_time, "%H:%M:%S")

			# Calculate the duration in minutes
			duration_hours = (to_time - from_time).total_seconds() 

			# Format the duration with two decimal places
			formatted_duration = "{:.2f}".format(duration_hours)

			# Set the formatted duration in the document's field
			self.duration = formatted_duration	
		
		
	def validate_time(self):
		if self.from_time > self.to_time:
			frappe.throw(_("From Time must be earlier than To Time."))

	def check_for_conflicting_meetings(self):
		# Check for other meetings on the same date and time
		conflicting_meetings = frappe.get_all("Meeting",
		filters={
			"date": self.date,
			"from_time": (">=", self.from_time),
			"to_time": ("<=", self.to_time),
			"name": ("!=", self.name),  # Exclude the current meeting
		},
		fields=["name"]
		)

		if conflicting_meetings:
			frappe.throw(_("There is a conflicting meeting scheduled for the same time on the same day. Please choose a different date or time."))

	"""
	def on_update(self):
		#	self.sync_todos()
		#	self.send_minutes()
	"""
	
	def validate_attendees(self):
		"""Set missing names and warn if duplicate"""
		found = []
		for attendee in self.attendees:
			if not attendee.full_name:
				attendee.full_name = get_full_name(attendee.attendee)

			if attendee.attendee in found:
				frappe.throw(_("Attendee {0} entered twice").format(attendee.attendee))

			found.append(attendee.attendee)
	"""
	def sync_todos(self):
		
		todos_added = [todo.name for todo in
			frappe.get_all("ToDo",
				filters={
					"reference_type": self.doctype,
					"reference_name": self.name,
					"assigned_by": ""
				})
			]

		for minute in self.minutes:
			if minute.assigned_to and minute.status=="Open":
				if not minute.todo:
					todo = frappe.get_doc({
						"doctype": "ToDo",
						"description": minute.description,
						"reference_type": self.doctype,
						"reference_name": self.name,
						"owner": minute.assigned_to
					})
					todo.insert()

					minute.db_set("todo", todo.name, update_modified=False)

				else:
					todos_added.remove(minute.todo)

			else:
				minute.db_set("todo", None, update_modified=False)

		for todo in todos_added:
			# remove closed or old todos
			todo = frappe.get_doc("ToDo", todo)
			todo.flags.from_meeting = True
			todo.delete()

	def get_context(self, context):
		context.parents = [{"name": "meetings", "title": "Meetings"}]
	"""

@frappe.whitelist()
def get_full_name(attendee):
	user = frappe.get_doc("User", attendee)

	# concatenates by space if it has value
	return " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))
	
