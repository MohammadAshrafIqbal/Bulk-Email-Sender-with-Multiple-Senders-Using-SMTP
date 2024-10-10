# Bulk-Email-Sender-with-Multiple-Senders-Using-SMTP

This Python script allows you to send personalized HTML emails to multiple recipients from a pool of sender email addresses, using the SMTP protocol. It supports:

Randomized Sender Emails: The script randomly selects one of the configured sender email addresses to send each email, adding an extra layer of variability.
Customizable HTML Email Template: You can design your email using full HTML, making the email visually appealing with custom content.
Email Personalization: The recipient’s name is extracted from their email address and can be included in the email content for a personal touch.
Recipient List: The recipient email addresses are loaded from a text file (emails.txt).
Error Handling: The script includes basic error handling for SMTP authentication issues and recipient address verification.
Features
Randomized sender email selection
HTML email support with customizable templates
Email personalization (based on recipient email address)
Error handling for common SMTP issues
Compatible with any SMTP service (currently using Hostinger as an example)
How to Use
Add your sender email addresses to the sender_emails list.
Place the recipient emails in a text file named emails.txt.
Customize the html_content_template with your desired email content and format.
Update your SMTP server details (smtp_server, port, and password).
Run the script to send the emails!
