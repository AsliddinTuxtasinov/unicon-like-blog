from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import EmailMessages
from .utils import send_email_with_attachment


@receiver(post_save, sender=EmailMessages)
def send_email_on_post_creation(sender, instance, created, **kwargs):
    if created:
        message_text = f"FISH/Tashkilot nomi: {instance.name}\n" \
                       f"E-mail: {instance.email}\n" \
                       f"Tel: {instance.phone_number}\n" \
                       f"Xabbar: {instance.message}\n" \
                       f"Yuborilgan vaqti:{instance.created_add}"

        send_email_with_attachment(
            subject=f"FISH/Tashkilot nomi: {instance.name}",
            message=message_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.services.email],
            file_path=instance.file.path,
        )
