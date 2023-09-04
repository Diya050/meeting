import frappe
from frappe import _
from frappe.utils import get_fullname, get_link_to_form
from frappe.utils import nowdate, add_days
from frappe.utils import get_datetime, now_datetime
from datetime import datetime, timedelta


@frappe.whitelist()
def send_invitation_emails(meeting):
	meeting = frappe.get_doc("Meeting", meeting)
	sender_fullname = get_fullname(frappe.session.user)

	if meeting.status == "Planned":
		if meeting.attendees:
				message = frappe.get_template("templates/emails/meeting_invitation.html").render({
					"sender":sender_fullname,
					"date":meeting.date,
					"from_time":meeting.from_time,
					"to_time":meeting.to_time,
					"invitation_message":meeting.invitation_message,
					"agenda": meeting.agenda,
				})
				frappe.sendmail(
				recipients=[d.attendee for d in meeting.attendees],
				sender=frappe.session.user,
				subject="New Meeting:" + meeting.title,
				message=message,
				reference_doctype=meeting.doctype,
				reference_name=meeting.name,
				)
				meeting.status = "Invitation Sent"
				meeting.save()
				frappe.msgprint(_("Invitation Sent"))
		else:
			frappe.msgprint("Enter atleast one Attendee for Sending")
	else:
		frappe.msgprint(_("Meeting Status must be 'Planned'"))

@frappe.whitelist()
def send_minutes(meeting):
	meeting = frappe.get_doc("Meeting", meeting)
	sender_fullname = get_fullname(frappe.session.user)
	if meeting.status == "Completed":
		if meeting.minutes:
			for d in meeting.minutes:
				message = frappe.get_template("templates/emails/minute_notification.html").render({
					"sender":sender_fullname,
					"action": d.action,
					"description": d.description,
					"complete_by":d.complete_by
				})
				frappe.sendmail(
					recipients=d.assigned_to,
					sender=frappe.session.user,
					subject=meeting.title,
					message=message,
					reference_doctype=meeting.doctype,
					reference_name=meeting.name,
					)
			meeting.status = "Minutes Sent"
			meeting.save()
			frappe.msgprint(_("Minutes Sent"))
		else:
			frappe.msgprint("Enter atleast one Minute for Sending")
	else:
		frappe.msgprint(_("Meeting Status must be 'Completed'"))


@frappe.whitelist()
def start_meeting_message(meeting):
    meeting = frappe.get_doc("Meeting", meeting)

    if meeting.status == "Invitation Sent":
        current_time = now_datetime()
        meeting_from_time = get_datetime(str(meeting.date) + ' ' + str(meeting.from_time))  # Convert to str

        if current_time > meeting_from_time:
            delay_seconds = (current_time - meeting_from_time).seconds

            if -120 <= delay_seconds <= 300:  # Tolerance window: -2 minutes to 5 minutes
                message = "Meeting is starting on time."
            else:
                delay_minutes = delay_seconds / 60
                message = f"The meeting is starting {delay_minutes:.1f} minutes late. Meeting has started."
        else:
            message = "Meeting has started."

        for attendee in meeting.attendees:
            frappe.publish_realtime(event="meeting_started", message=message, user=attendee.attendee)
            
        for attendee in meeting.attendees:
            frappe.sendmail(
                recipients=[attendee.attendee],
                sender=frappe.session.user,
                subject="Meeting Started: " + meeting.title,
                message=message
            )


        meeting.status = "In Progress"
        meeting.save()
        frappe.msgprint(_("Meeting Status updated to 'In Progress'"))
    else:
        frappe.msgprint(_("Meeting Status must be 'Invitation Sent' to start the meeting"))



@frappe.whitelist()
def get_meetings(start, end):
	if not frappe.has_permission("Meeting", "read"):
		raise frappe.PermissionError

	return frappe.db.sql("""select
		timestamp(`date`, from_time) as start,
		timestamp(`date`, to_time) as end,
		name,
		title,
		status,
		0 as all_day
	from `tabMeeting`
	where `date` between %(start)s and %(end)s""", {
		"start": start,
		"end": end
	}, as_dict=True)

def make_orientation_meeting(doc, method):
	"""Create an orientation meeting when a new User is added"""
	meeting = frappe.get_doc({
		"doctype": "Meeting",
		"title": "Orientation for {0}".format(doc.first_name),
		"date": add_days(nowdate(), 1),
		"from_time": "09:00",
		"to_time": "09:30",
		"status": "Planned",
		"attendees": [{
			"attendee": doc.name
		}]
	})
	# the System Manager might not have permission to create a Meeting
	meeting.flags.ignore_permissions = True
	meeting.insert()

	frappe.msgprint(_("Orientation meeting created"))

def update_minute_status(doc, method=None):
	"""Update minute status to Closed if ToDo is closed or deleted"""
	if doc.reference_type != "Meeting" or doc.flags.from_meeting:
		return

	if method=="on_trash" or doc.status=="Closed":
		meeting = frappe.get_doc(doc.reference_type, doc.reference_name)
		for minute in meeting.minutes:
			if minute.todo == doc.name:
				minute.db_set("todo", None, update_modified=False)
				minute.db_set("status", "Closed", update_modified=False)
