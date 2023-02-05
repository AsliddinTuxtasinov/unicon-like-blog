from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import EmailMessages
from .utils import send_email_with_attachment


@receiver(post_save, sender=EmailMessages)
def send_email_on_post_creation(sender, instance, created, **kwargs):
    if created:

        send_email_with_attachment(
            subject=instance.title,
            message=f"Tashkilot nomi: {instance.name_organization}\nFISH: {instance.full_name}\nE-mail: {instance.email}\nTel: {instance.phone_number}\nXabar: {instance.message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.services.email],
            file_path=instance.file.path,
        )
