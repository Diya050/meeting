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
                "sender": sender_fullname,
                "start_datetime": meeting.start_datetime,
                "end_datetime": meeting.end_datetime,
                "invitation_message": meeting.invitation_message,
                "agenda": meeting.agenda,
                "supplementary_agenda": meeting.supplementary_agenda,
                "by_chairman_permission": meeting.by_chairman_permission,
            })

            frappe.sendmail(
                recipients=[d.attendee for d in meeting.attendees],
                sender=frappe.session.user,
                subject="New Meeting: " + meeting.title,
                message=message,
                reference_doctype=meeting.doctype,
                reference_name=meeting.name,
            )

            meeting.status = "Invitation Sent"
            meeting.save()
            frappe.msgprint(_("Invitation Sent"))
        else:
            frappe.msgprint("Enter at least one Attendee for Sending")
    else:
        frappe.msgprint(_("Meeting Status must be 'Planned'"))

		
@frappe.whitelist()
def end_meeting_message(meeting):
    meeting = frappe.get_doc("Meeting", meeting)
    if meeting.status == "In Progress":
        message = "Ladies and Gentlemen, as we conclude today's meeting, I want to express gratitude to those who actively participated. For those who couldn't make it, we missed your presence and contributions. If you have any questions or need a recap, please feel free to connect with us. Thank you for your understanding."
        for attendee in meeting.attendees:
            frappe.publish_realtime(event="meeting_ended", message=message, user=attendee.attendee)
            
        for attendee in meeting.attendees:
            frappe.sendmail(
                recipients=[attendee.attendee],
                sender=frappe.session.user,
                subject="Meeting Ended: " + meeting.title,
                message=message
            )
        meeting.status = "Completed"
        meeting.save()
        frappe.msgprint(_("Meeting Status updated to 'Completed'"))
    else:
        frappe.msgprint(_("Meeting Status must be 'In Progress' to end the meeting"))


	
@frappe.whitelist()
def send_minutes(meeting):
	meeting = frappe.get_doc("Meeting", meeting)
	sender_fullname = get_fullname(frappe.session.user)

	if meeting.status == "Completed":
		if meeting.agenda:
			# Prepare a message with a table containing all meeting minutes
			message = frappe.get_template("templates/emails/minute_notification.html").render({
				"sender": sender_fullname,
				"meeting_title": meeting.title,
				"minutes_list": meeting.agenda,
			})

			# Get a list of all attendees
			attendees = [attendee.attendee for attendee in meeting.attendees]

			frappe.sendmail(
				recipients=attendees,
				sender=frappe.session.user,
				subject="Meeting Minutes: " + meeting.title,
				message=message,
				reference_doctype=meeting.doctype,
				reference_name=meeting.name,
			)

			meeting.status = "Minutes Sent"
			meeting.save()
			frappe.msgprint(_("Minutes Sent"))
		else:
			frappe.msgprint("Enter at least one Minute for Sending")
	else:
		frappe.msgprint(_("Meeting Status must be 'Completed'"))



@frappe.whitelist()
def start_meeting_message(meeting):
    meeting = frappe.get_doc("Meeting", meeting)

    if meeting.status == "Invitation Sent":
        current_time = now_datetime()

        if current_time >= meeting.start_datetime and current_time <= meeting.end_datetime:
            delay_seconds = (current_time - meeting.start_datetime).seconds

            if -120 <= delay_seconds <= 300:  # Tolerance window: -2 minutes to 5 minutes
                message = "Ladies and Gentlemen, I am pleased to announce the commencement of our meeting, which is on time. Your presence is requested in the meeting room, and we anticipate your active involvement in the proceedings. Thank you for your attention and cooperation."
            else:
                delay_minutes = delay_seconds / 60
                message = f"Ladies and Gentlemen, I am pleased to announce the commencement of our meeting, which is starting after a delay of {delay_minutes:.1f} minutes. Your presence is requested in the meeting room, and we anticipate your active involvement in the proceedings. Thank you for your patience and cooperation."
        else:
            message = "Ladies and Gentlemen, I am pleased to announce the commencement of our meeting, which is on time. Your presence is requested in the meeting room, and we anticipate your active involvement in the proceedings. Thank you for your attention and cooperation."

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
        start_datetime as start,
        end_datetime as end,
        name,
        title,
        status,
        0 as all_day
    from `tabMeeting`
    where start_datetime between %(start)s and %(end)s""", {
        "start": start,
        "end": end
    }, as_dict=True)

"""
def make_orientation_meeting(doc, method):
	# Create an orientation meeting when a new User is added
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
"""
"""
def update_minute_status(doc, method=None):
	# Update minute status to Closed if ToDo is closed or deleted
	if doc.reference_type != "Meeting" or doc.flags.from_meeting:
		return

	if method=="on_trash" or doc.status=="Closed":
		meeting = frappe.get_doc(doc.reference_type, doc.reference_name)
		for minute in meeting.minutes:
			if minute.todo == doc.name:
				minute.db_set("todo", None, update_modified=False)
				minute.db_set("status", "Closed", update_modified=False)
				
"""
"""
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
		frappe.msgprint(_("Meeting Status must be 'Completed'"))"""
