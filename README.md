# Meeting App

>"Power Up Your Meetings with Frappe's Meeting App!"

Are your meetings feeling mundane and unproductive? Say hello to a game-changer in the world of meeting management! This document provides an in-depth guide on how to use the Meeting app created with Frappe Framework. From seamless invitations to effortless minute-taking, this app will revolutionize the way you meet. Get ready to elevate your meetings to a whole new level!

## Installation

- Set up frappe-bench using [Install frappe](https://github.com/D-codE-Hub/Frappe-ERPNext-Version-14--in-Ubuntu-22.04-LTS)
- Create a site for installing Meeting app:
  ```bash
  $ cd frappe-bench
  $ bench new-site meeting.com
  # Set administrator password and it will be the password for your site with username "administrator"
  $ bench get-app https://github.com/Diya050/meeting.git
  $ bench --site meeting.com install-app meeting
  ```
- Now open site and use app:
  ```bash
  $ bench use meeting.com
  $ bench start
  ```
- Your app is running at 127.0.0.1:8000
- Go to http://127.0.0.1:8000/app/meeting for creating new meetings.

## Key Features:
- **Easy Installation:** Setting up the Meeting App is a breeze with clear installation instructions.

- **User Management:** Admins can create and manage users, granting specific roles and permissions as needed.

- **Meeting Creation:** Create and schedule meetings effortlessly, including setting agendas and invitation messages.

- **Real-time Updates:** Monitor meeting progress in real-time through the "See on website" feature.

- **Invitation Management:** Easily add attendees, whether individuals or groups, and send out invitations with just a click.

- **Email Notifications:** Attendees receive emails at various stages of the meeting, including invitations, start notifications, and minutes.

- **Meeting Status:** Keep track of meeting status, from "Planned" to "In Progress" to "Completed."

- **Minutes Management:** Record and manage meeting minutes, with options to add actions, descriptions, and more.

- **Automatic Calculations:** The app automatically calculates meeting duration based on start and end times.

- **Meeting History:** Access a list of past meetings with their respective statuses in different colors for easy reference.

- **Mark Attendance:** In the Attendees Section, there is checkbox for whether invitation accepted or not and whether meeting attended or not.

- **Organized Meeting Records:** Easily access past meeting records and minutes, making it simple to reference previous discussions and decisions.

- **User-friendly Interface:** The app offers an intuitive interface that is easy to navigate for both administrators and attendees.

- **Flexibility:** The ability to add supplementary agendas and permissions enhances the app's flexibility to accommodate different meeting scenarios.


## Getting Started

1. [As the Administrator](manuals./administrator.md)
2. [As the Meeting Manager](manuals./manager.md)
3. [As a Meeting Attendee](manuals./attendee.md)

