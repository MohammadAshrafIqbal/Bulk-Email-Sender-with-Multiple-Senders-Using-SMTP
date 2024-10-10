import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# List of sender emails
sender_emails = [
    "Sender1@yourmail.com",
    "Sender2@yourmail.com",
    "Sender3@yourmail.com",
    "Sender4@yourmail.com",
    "Sender5@yourmail.com",
    "Sender6@yourmail.com"
]

# Shared password and SMTP server details for Hostinger
password = "user_name"
smtp_server = "smtp.hostinger.com" #Add Your smtp Currently Added hostinger server
port = 465

# Read recipient emails from file
with open('emails.txt', 'r') as file:
    recipients = [line.strip() for line in file if line.strip()]

# HTML email content template
html_content_template = """
<html>
  <body>
    <p>Add your Stuff You Can Use Full Html Code And Design Here And Make Beautiful Template Of Email</p>
  </body>
</html>
"""

# Function to extract name from email address
def extract_name(email):
    name = email.split('@')[0]
    return name.replace('.', ' ').title()

# Function to send an email
def send_email(sender_email, recipient, html_content):
    try:
        with smtplib.SMTP_SSL(smtp_server, port) as connection:
            connection.login(user=sender_email, password=password)
            
            # Create email message
            msg = MIMEMultipart('alternative')
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = 'Give Your Subject!'
            
            # Attach the personalized HTML message
            msg.attach(MIMEText(html_content, 'html'))
            
            # Send the email
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=recipient,
                msg=msg.as_string()
            )
            print(f"Email sent to: {recipient} from {sender_email}")
    except smtplib.SMTPAuthenticationError:
        print(f"Authentication error for sender {sender_email}. Check the credentials.")
    except smtplib.SMTPRecipientsRefused:
        print(f"Recipient address {recipient} refused. Verify the email address.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred while sending to {recipient} from {sender_email}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Send the email to each recipient individually
for recipient in recipients:
    recipient_name = extract_name(recipient)
    html_content = html_content_template.format(name=recipient_name)
    
    # Randomly select a sender email
    sender_email = random.choice(sender_emails)
    
    send_email(sender_email, recipient, html_content)

print("All emails sent successfully (or attempted).")
