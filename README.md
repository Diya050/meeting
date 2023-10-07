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

## Getting Started

This section will guide you through the initial setup and help you get started with creating and managing meetings.

- Log in to your Frappe instance as a user with the necessary permissions.
 
![login_page](meeting/images/meeting1.png)![meeting1](https://github.com/Diya050/meeting/assets/124448340/1a7402f1-8dfa-4a24-af51-6e759981ff04)

  
- If you are the Meeting Manager then you have to create users with role Meeting Attendee whom you wish to invite for a meeting in future.
  
- You also have to manage the permissions that you want to give to each user.

- From the Frappe Desk, from awesome bar navigate to "Meeting List > New Meeting" to create a new meeting.

![awesome_bar](meeting/images/meeting2.png)![meeting2](https://github.com/Diya050/meeting/assets/124448340/563d840c-efe4-4b5b-8ae3-717c7ccf4f1d)

- Click `Create your first Meeting` to create a meeting:

![create_meetings](meeting/images/meeting3.png)![meeting3](https://github.com/Diya050/meeting/assets/124448340/eeec4441-76bb-4212-82a1-720bc38202b4)

- This will open a dashboard. Fill the Meeting Title, choose meeting status as planned initially, click see on website (so that it is viewed to all), set date and time (Duration will be calculated automatically), set Agenda and add Invitation Message. Save all these changes.

![meeting_details](meeting/images/meeting4.png)![meeting4](https://github.com/Diya050/meeting/assets/124448340/fbb2acca-2b30-4627-9a37-2e4268544976)

- This how meeting details would look like on website:

  ![website_view](meeting/images/meeting5.png)![meeting5](https://github.com/Diya050/meeting/assets/124448340/e8c5b41c-7949-44fb-89c2-de4e38462a27)

- Here is how your past meetings can be accessed in the form of list with their statuses in different colours.

  ![meetings_list](meeting/images/meeting6.png)![meeting6](https://github.com/Diya050/meeting/assets/124448340/a77afa69-fada-4f93-86eb-22783caf9444)

- Now since you have planned the meeting, its time to add attendees and send them invitations for the meeting.
  
