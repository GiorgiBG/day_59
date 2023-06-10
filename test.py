import smtplib
from email.message import EmailMessage

class SendMail:
    def __init__(self, mobile, body, name):
        self.from_addr = "giorgi_bgujito@yahoo.com"
        self.to_addr = "giorgibgujito@gmail.com"
        self.subject = f"{mobile} {name}"
        self.body = body
        self.name = name



    def send_mail(self):
        # SMTP server configuration
        smtp_server = "smtp.mail.yahoo.com"
        smtp_port = 587

        # Login credentials (if required)

        # Create the email message
        msg = EmailMessage()
        msg.set_content(self.body)
        msg["Subject"] = self.subject
        msg["From"] = self.from_addr
        msg["To"] = self.to_addr

        # Create SMTP connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption

        # Login to the SMTP server (if required)
        username = "giorgi_bgujito@yahoo.com"
        password = "yeqnupmkzsubzeyo"
        server.login(username, password)

        # Send the email
        server.send_message(msg)

        # Close the SMTP connection
        server.quit()








