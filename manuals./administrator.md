# Getting Started as Administrator

This section will guide you through the initial setup and help you get started with creating and managing meetings.

- Log in to your Frappe instance as administrator.
 
![meeting1](https://github.com/Diya050/meeting/assets/124448340/eaff4230-6b6f-42fc-b873-bb6aad6ff02e)


  
- You have to create users with role Meeting Manager and Meeting Attendees whom you wish to invite for a meeting in future.
  
- You also have to manage the permissions that you want to give to each user and set up email account of each user.

- Being an administrator, you can access `Meeting` doctype and make changes when required.

- In the sidebar, navigate to the `Meeting Workspace` section, where you'll find convenient shortcuts to access the list of meetings, a direct link to your website showcasing past meetings, and informative statistics summarizing your meeting history.

![Screenshot from 2024-01-25 12-22-24](https://github.com/Diya050/meeting/assets/124448340/b43a6f8e-d084-4b60-a934-b2093552318c)

<br>

![image](https://github.com/Diya050/meeting/assets/124448340/531ae645-88d1-4d14-ac39-69509b4150df)

- By clicking on `View Website`, it will show all the past meetings(created by all the users) at route /meeting:

  ![image](https://github.com/Diya050/meeting/assets/124448340/df787df4-19bb-42e5-ad22-5273cdbee94c)


- To create a new meeting, you have two options:
   - Toggle over to the `Meetings list` section in the Meeting Workspace and click on the `+` sign.
   - Click on `View List` in the `Meeting list` section and then select `Create your first Meeting` to initiate the meeting creation process.

![image](https://github.com/Diya050/meeting/assets/124448340/3bca04ad-cb24-48a1-a3f3-e52bcda13c3d)

![image](https://github.com/Diya050/meeting/assets/124448340/444d4ac1-ca9c-4e10-a554-1d2edfc4a6ab)

<br>

- If it's your first meeting:
  
![meeting3](https://github.com/Diya050/meeting/assets/124448340/a5585bee-012f-4217-8077-bc30f484d9a6)

- To create meetings, further:
  
![Screenshot from 2024-01-25 12-31-24](https://github.com/Diya050/meeting/assets/124448340/cfa135bf-3b69-46a3-9518-55ad13d91bc6)


- This will open a dashboard. Fill the Meeting Title, choose a Venue, Committee Name, meeting status is planned(by default and will change automatically according to the meeting's progress), check `Show in website` (so that it is viewed to all the attendees through website), set start date and time, and end date and time(Duration will be calculated automatically), set Agenda, and edit Invitation Message(if required). Save all these changes.

  
![image](https://github.com/Diya050/meeting/assets/124448340/ef0be91c-8af6-4d3c-9385-c103d662413d)

![image](https://github.com/Diya050/meeting/assets/124448340/3ab1177e-7817-43e1-af97-104e80baa905)

![image](https://github.com/Diya050/meeting/assets/124448340/df727063-912e-4ed2-baaf-51541d733bf4)


`Note:` Kindly, do not do any changes to content inside {{ }} in invitation message.


- You could see your Meeting Progress on website, by clicking on `See on website` in the panel on the left side. This website link would be shared with all your attendees through the invitation message, so that they could trace the progress of meeting. If you uncheck `Show in website`, your meeting details would be removed from website.
  
![image](https://github.com/Diya050/meeting/assets/124448340/c8ac8e89-1f6e-49d7-96c3-f4951fce1d52)

![image](https://github.com/Diya050/meeting/assets/124448340/461f3b2a-0e8c-411e-a36e-0962334ed358)

![image](https://github.com/Diya050/meeting/assets/124448340/85826107-c90e-4b57-8c07-2aaf0b488bd3)

- Here is how your past records of your meetings can be accessed in the form of list with their statuses in different colours.

![meeting6](https://github.com/Diya050/meeting/assets/124448340/dc9766a2-ea11-4ed1-9ebc-349be02cf9b8)



- Now since you have planned the meeting, its time to add attendees and send them invitations for the meeting. You can add as many attendees as you want by making them users of your frappe app. You can even add groups like a Google Group as an user by adding its email to send invitation to all the members in the group.

![image](https://github.com/Diya050/meeting/assets/124448340/c9c2d3f1-670f-4e7c-a77a-0d5208dd28fa)


- Now you just have to click `Send Emails` button. With this emails would sent to all attendees and status of the Meeting would change to `Invitation Sent`.
  
![image](https://github.com/Diya050/meeting/assets/124448340/df727063-912e-4ed2-baaf-51541d733bf4)

![meeting9](https://github.com/Diya050/meeting/assets/124448340/ab396c7a-1cbb-4397-b58d-d38d0a1b6456)



- Here's a view of your invitation email in your attendees' inbox:

![image](https://github.com/Diya050/meeting/assets/124448340/91dfea11-0ddf-40c1-83cb-becbb4bcf7fe)
![image](https://github.com/Diya050/meeting/assets/124448340/567f577a-f64e-478a-ad53-12ce26e6d29c)


- Click on `Start Meeting` button below `Show in Webite`. This will send a "Start Meeting" email to all your attendees and also display a real-time message to all your attendees who are currently online on the website. This also changes the Meeting status to `In Progress`.

![image](https://github.com/Diya050/meeting/assets/124448340/8f717890-92ae-4b03-9e43-7cb3cd0661d7)

![image](https://github.com/Diya050/meeting/assets/124448340/bfccf2d2-5968-4f3b-bb62-9da8f9d0acf4)


- Here's a view of your `Meeting Started` email in your attendees' inbox (it also mentions whether the meeting was started on time or was late):

![image](https://github.com/Diya050/meeting/assets/124448340/bd575709-c428-48f0-b08b-eb592d75dd13)


- While the meeting is `In Progress`, you can mark attendance of attendees(by checking boxes in Attendee Section) and you can type the minutes in the `Minutes Section` but you could send them only after the meeting is completed.

  ![image](https://github.com/Diya050/meeting/assets/124448340/6bd3bc9d-e7f3-434f-9f4a-cce9b73dda77)

- You can add minute description, choose the corresponding action taken, mention Assigned to (some attendee if any) and set date i.e Completed by.

![image](https://github.com/Diya050/meeting/assets/124448340/f382f3cc-48ab-4a64-9aa0-a5c1d52037b8)

![image](https://github.com/Diya050/meeting/assets/124448340/92a857db-eeda-4a80-89fd-298dd4750900)

- When the meeting ends, you can click the `End Meeting` button below the status bar. This will send a "Meeting Ended" message to all the attendees and change the meeting status to `Completed`.
  
![image](https://github.com/Diya050/meeting/assets/124448340/e822afc2-f9d8-4c66-b2e3-af4797e29346)

![image](https://github.com/Diya050/meeting/assets/124448340/c6696ca9-4ccf-48cf-99f6-1c7d9dc862f6)


- Here's a view of your `Meeting Ended` email in your attendees' inbox:

![image](https://github.com/Diya050/meeting/assets/124448340/15a7be71-89d0-4905-9efc-43dd1f84d4f0)

- Now you will be able to view `Send Minutes` button in the `Agenda and Minutes` Section since the status of your meeting is now "Completed". 

- When you click `Send Minutes` button, minutes of meeting would be sent to all attendees and meeting status would change to `Minutes Sent`.
  
![image](https://github.com/Diya050/meeting/assets/124448340/4ce6d588-1ad8-4bf6-9cbb-3978925d29c1)

![image](https://github.com/Diya050/meeting/assets/124448340/a3ff6f46-77ab-42c4-9afd-df1fef22da6a)


- Here's a view of your `Meeting Minutes` email in your attendees' inbox:
  
![image](https://github.com/Diya050/meeting/assets/124448340/3ff9061f-e4c9-44a9-82b9-bdab1028f496)


- You can also add "Supplementary Agenda" and "Agenda By Chairman Permission" if any, at any time and send them by changing meeting status to `Planned`. Saving changes. Clicking `Send Emails` button in Invitation Section.

- This app also makes sure that you do not plan a meeting on the sames date, time and at the same venue, thus preventing clashing meetings.

- If you create a meeting of same name it will automatically add suitable suffix to it's name.

- It generates unique route for each meeting, thus enhacing privacy. Also, meetings created by a particular user could be viewed by him/her only on the desk. But administrator could view all the meetings.

- You can also obtain a pdf of your progress by clicking `Print icon`>>`Pdf Button`: 

![image](https://github.com/Diya050/meeting/assets/124448340/80d54663-deac-41c4-991d-833a17986ed6)

![image](https://github.com/Diya050/meeting/assets/124448340/1b0fa92c-882e-4458-81eb-6e498807bf2f)

![image](https://github.com/Diya050/meeting/assets/124448340/5f19711a-8771-4812-9722-55551791c67b)

> To clinch it all, the Meeting App powered by the Frappe Framework is your go-to solution for revolutionizing the way you manage and conduct meetings. This comprehensive documentation has provided you with a step-by-step guide on how to install, set up, and make the most of this powerful tool.
