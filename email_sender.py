import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email
def send_email(to_email, subject, message):
    # Replace these placeholders with your email configuration
    email_sender = "shivarapolu1729@gmail.com"
    email_password = "Shiva.@1729"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    # Setup the server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_sender, email_password)

    # Send the email
    server.sendmail(email_sender, to_email, msg.as_string())
    server.quit()
