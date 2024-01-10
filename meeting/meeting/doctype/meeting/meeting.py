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
from frappe import Redirect


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
  


	def get_context(self, context):
		# Check if the user is logged in
		if frappe.session.user:
			# Check if the user has the required permission to view the meeting
			if self.has_permission("read"):
		                # If the user is logged in and has permission, set the context for the template
				context.show_meeting = True
				context.meeting_data = {
					"title": self.title,
					"start_datetime": self.start_datetime,
					"end_datetime": self.end_datetime,
				}
			else:
				# If the user doesn't have permission, set a flag to hide the meeting content
				context.show_meeting = False
		else:
			# If the user is not logged in, redirect them to the login page
			frappe.local.flags.redirect_location = '/login'
			raise frappe.Redirect


	def has_permission(self, ptype="read", user=None):
		# Check if the user has the required permission
		return frappe.has_permission(self.doctype, ptype, self, user=user)


	def before_save(self):
		# Calculate the duration if both start_datetime and end_datetime are set
		if self.start_datetime and self.end_datetime:
			start_datetime = datetime.strptime(self.start_datetime, '%Y-%m-%d %H:%M:%S')
			end_datetime = datetime.strptime(self.end_datetime, '%Y-%m-%d %H:%M:%S')

			duration_minutes = (end_datetime - start_datetime).total_seconds()

			formatted_duration = "{:.2f}".format(duration_minutes)

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
	
	
@frappe.whitelist(allow_guest=True)
def check_user_login():
	if frappe.session.user:
		# User is logged in, return your meeting content here
		meeting_content = get_meeting_content()
		return frappe._dict(content=meeting_content)
	else:
		# User is not logged in, return a response or redirect as needed
		frappe.respond_as_web_page(_('Login Required'), _('Please log in to access the meeting.'), http_status_code=401)

def get_meeting_content():
	# Your logic to fetch and return meeting content
	# For example, you can query the Meeting doctype and return relevant data
	meetings = frappe.get_list('Meeting', fields=['name', 'title', 'start_datetime'], limit=5)
	return meetings
	
