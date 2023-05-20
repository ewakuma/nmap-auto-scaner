import smtplib as smtp

def send_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email, recipient_name, message):
    with smtp.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.encode('utf-8'))
