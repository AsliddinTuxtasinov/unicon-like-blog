from django.core.mail import EmailMessage


def send_email_with_attachment(subject, message, from_email, recipient_list, file_path):
    # create an EmailMessage object with the given subject, message, and sender and recipient email addresses
    email = EmailMessage(subject, message, from_email, recipient_list)

    # attach the file at the given file path to the email
    email.attach_file(file_path)

    # send the email
    email.send()
