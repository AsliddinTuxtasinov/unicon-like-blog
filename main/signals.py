from email.message import EmailMessage

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import EmailMessages
from django.core.mail import EmailMessage as sendMail


@receiver(post_save, sender=EmailMessages)
def send_email_on_post_creation(sender, instance, created, **kwargs):
    if created:
        message_text = f"FISH/Tashkilot nomi: {instance.name}\n" \
                       f"E-mail: {instance.email}\n" \
                       f"Tel: {instance.phone_number}\n" \
                       f"Xabbar: {instance.message}\n" \
                       f"Yuborilgan vaqti:{instance.created_add}"

        # create an EmailMessage object with the given subject, message, and sender and recipient email addresses
        email = sendMail(
            subject=f"FISH/Tashkilot nomi: {instance.name}",
            body=message_text,
            from_email=settings.EMAIL_HOST_USER,
            to=[instance.services.email],
        )

        # attach the file at the given file path to the email
        if instance.file:
            file_instance = instance.file.path
            email.attach_file(file_instance)

        # send the email
        email.send()

