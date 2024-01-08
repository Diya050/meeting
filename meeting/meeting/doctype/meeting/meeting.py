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
from datetime import datetime, timedelta

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
		base_name = title.replace(' ', '_')
		unique_name = base_name
		if self.is_new():
			counter = 1

			while frappe.get_all("Meeting", filters={"name": unique_name}):
				counter += 1
				unique_name = f"{base_name.title()} No. {counter}"
			updated_title = unique_name.replace('-', ' ')
		
			return unique_name, updated_title
		else:	
			return self.name, self.title
  


	def before_save(self):
		# Calculate the duration if both start_datetime and end_datetime are set
		if self.start_datetime and self.end_datetime:
			start_datetime = datetime.strptime(self.start_datetime, '%Y-%m-%d %H:%M:%S')
			end_datetime = datetime.strptime(self.end_datetime, '%Y-%m-%d %H:%M:%S')

			# Calculate the duration in minutes
			duration_minutes = (end_datetime - start_datetime).total_seconds()

			# Format the duration with two decimal places
			formatted_duration = "{:.2f}".format(duration_minutes)

			# Set the formatted duration in the document's field
			self.duration = formatted_duration


	
		
		
	def validate_time(self):
		if self.start_datetime and self.end_datetime and self.start_datetime >= self.end_datetime:
			frappe.throw(_("Start time must be earlier than end time."))



	def check_for_conflicting_meetings(self):
		# Check for other meetings on the same date and time
		conflicting_meetings = frappe.get_all("Meeting",
		filters={
			"start_datetime": ("between", [self.start_datetime, self.end_datetime]),
			"name": ("!=", self.name),  # Exclude the current meeting
		},
		fields=["name"]
		)
    
		if conflicting_meetings:
			frappe.throw(_("There is a conflicting meeting scheduled for the same time. Please choose a different date or time."))


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
	
