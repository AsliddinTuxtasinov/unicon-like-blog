from django.core.mail import EmailMessage
from rest_framework import validators, status


def send_email_with_attachment(subject, message, from_email, recipient_list, file_path):
    # create an EmailMessage object with the given subject, message, and sender and recipient email addresses
    email = EmailMessage(subject, message, from_email, recipient_list)

    # attach the file at the given file path to the email
    email.attach_file(file_path)

    # send the email
    email.send()


def error_response_404():
    raise validators.ValidationError(
        detail={"message": "Object is not found 404"}, code=status.HTTP_404_NOT_FOUND)
