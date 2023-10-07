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

- **Organized Meeting Records:** Easily access past meeting records and minutes, making it simple to reference previous discussions and decisions.

- **User-friendly Interface:** The app offers an intuitive interface that is easy to navigate for both administrators and attendees.

- **Flexibility:** The ability to add supplementary agendas and permissions enhances the app's flexibility to accommodate different meeting scenarios.


## Getting Started

This section will guide you through the initial setup and help you get started with creating and managing meetings.

- Log in to your Frappe instance as a user with the necessary permissions.
 
![meeting1](https://github.com/Diya050/meeting/assets/124448340/eaff4230-6b6f-42fc-b873-bb6aad6ff02e)


  
- If you are the Meeting Manager then you have to create users with role Meeting Attendee whom you wish to invite for a meeting in future.
  
- You also have to manage the permissions that you want to give to each user.

- From the Frappe Desk, through awesome bar navigate to "Meeting List > New Meeting" to create a new meeting.

![meeting2](https://github.com/Diya050/meeting/assets/124448340/79cb159a-6d71-4f0d-bb86-7cc5730fb050)


- Click `Create your first Meeting` to create a meeting:
  
![meeting3](https://github.com/Diya050/meeting/assets/124448340/a5585bee-012f-4217-8077-bc30f484d9a6)



- This will open a dashboard. Fill the Meeting Title, choose meeting status as planned initially, check `Show on website` (so that it is viewed to all), set date and time (Duration will be calculated automatically), set Agenda and add Invitation Message. Save all these changes.

![meeting4](https://github.com/Diya050/meeting/assets/124448340/b8c5e007-1cd0-4440-a9a0-6ffd569ab847)


- You could see your Meeting Progress on website, by clicking on `See on website` in the panel on the left side. Remember that only the meeting to which you have made the changes last would be viewed to all on the website.

![Screenshot from 2023-10-07 20-12-36](https://github.com/Diya050/meeting/assets/124448340/9e53c4a1-1ebe-4bb1-9ddf-150c44cebac0)


- Here is how your past records of your meetings can be accessed in the form of list with their statuses in different colours.

![meeting6](https://github.com/Diya050/meeting/assets/124448340/dc9766a2-ea11-4ed1-9ebc-349be02cf9b8)



- Now since you have planned the meeting, its time to add attendees and send them invitations for the meeting. You can add as many attendees as you want by making them users of your frappe app. You can even add groups like a GooGle Group as an user by adding its email to send invitation to all the members in the group.

![meeting7](https://github.com/Diya050/meeting/assets/124448340/adbdfff2-570d-4380-946e-fe55ff6c03ba)



- Now you just have to click `Send Emails` button. With this emails would sent to all attendees and status of the Meeting would change to `Invitation Sent`. 

![meeting8](https://github.com/Diya050/meeting/assets/124448340/a20e126e-013e-4af3-9069-e4ed4c4a3f39)

![meeting9](https://github.com/Diya050/meeting/assets/124448340/ab396c7a-1cbb-4397-b58d-d38d0a1b6456)



- Here a view of your invitation email in your attendees' inbox:

![meeting10](https://github.com/Diya050/meeting/assets/124448340/5524638c-0009-46b5-9c35-f2618ecc61a2)



- Click on `Start Meeting` button below status bar. This will send a "Start Meeting" email to all your attendees and also display a real-time message to all your attendees who are currently online on the website. This also changes the Meeting status to `In Progress`.

![meeting11](https://github.com/Diya050/meeting/assets/124448340/a121b3af-4190-4b6e-a4d3-175e65d39c8f)

![meeting12](https://github.com/Diya050/meeting/assets/124448340/81b67315-587c-46a1-9405-b45f23d7cf27)



- Here a view of your `Meeting Started` email in your attendees' inbox (it also mentions whether the meeting was started on time or was late):

![meeting13](https://github.com/Diya050/meeting/assets/124448340/1ea34e1e-639c-4b14-bd91-b1972b963e1c)



- While the meeting is `In Progress` you can type the minutes in the `Minutes Section` but you could send them only after the meeting is completed. You can add Actions, provide their Descriptions, give Status (as open or closed), mention Assigned to (some attendee if any) and set date i.e Completed by.

![meeting19](https://github.com/Diya050/meeting/assets/124448340/8479ec8b-84c6-428f-a469-835d33a0fcdb)



- When the meeting ends, you can click the `End Meeting` button below the status bar. This will send a "Meeting Ended" message to all the attendees and change the meeting status to `Completed`.

![meeting14](https://github.com/Diya050/meeting/assets/124448340/54872239-d4e4-4fad-a5bb-cb4204704a1d)

![meeting15](https://github.com/Diya050/meeting/assets/124448340/4f212c2a-847b-41b1-a102-067e628026b5)



- Here a view of your `Meeting Ended` email in your attendees' inbox:

![meeting16](https://github.com/Diya050/meeting/assets/124448340/8a3bcc26-118b-46a3-bfce-7ed7a44d25ee)



- Now you will be able to view `Send Minutes` button in the Minutes Section since the status of your is now "Completed". 

- When you click `Send Minutes` button, minutes of meeting would be sent to all attendees and meeting status would change to `Minutes Sent`.

![meeting17](https://github.com/Diya050/meeting/assets/124448340/47783303-29a2-496d-b230-fa78250a5650)



- Here a view of your `Meeting Minutes` email in your attendees' inbox:
  
![meeting18](https://github.com/Diya050/meeting/assets/124448340/e96b09ae-2688-4be2-b353-d6be458fe50d)



- You can also add "Supplementary Agenda" and "Agenda By Chairman Permission" if any at any time and send them by changing meeting status to `Planned`. Saving changes. Clicking `Send Emails` button in Invitation Section.


> To clinch it all, the Meeting App powered by the Frappe Framework is your go-to solution for revolutionizing the way you manage and conduct meetings. This comprehensive documentation has provided you with a step-by-step guide on how to install, set up, and make the most of this powerful tool.
