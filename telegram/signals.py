import asyncio
import threading
from aiogram import types

from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import EmailMessages
from telegram.bot import bot, dp
from telegram.models import TelegramBot

# Create a lock to control access to the function
lock = threading.Lock()

chat_ids = TelegramBot.objects.all()


async def send_message_to_telegram_bot(obj_id, message_text, file):
    with lock:
        sent_message = await bot.send_message(chat_id=obj_id.chat_id, text=message_text, parse_mode=types.ParseMode.HTML)
        await bot.send_document(chat_id=obj_id.chat_id, document=open(file, 'rb'), reply_to_message_id=sent_message.message_id)


def send_message_in_thread(obj_id, message_text, file_instance):
    asyncio.run(send_message_to_telegram_bot(obj_id=obj_id, message_text=message_text, file=file_instance))


@receiver(post_save, sender=EmailMessages)
def send_email_on_post_creation(sender, instance, created, **kwargs):
    if created:
        message_text = f"<b>Bo'lim: {instance.services.name}</b>\n" \
                       f"<b>Bo'lim email: {instance.services.email}</b>\n" \
                       f"<b>Tashkilot nomi: {instance.name_organization}</b>\n" \
                       f"<b>FISH: {instance.full_name}</b>\n" \
                       f"<b>E-mail: {instance.email}</b>\n" \
                       f"<b>Tel: {instance.phone_number}</b>\n" \
                       f"<b>Xabar: {instance.message}</b>"

        file_instance = instance.file.path

        if chat_ids:
            for obj_id in chat_ids:
                thread = threading.Thread(target=send_message_in_thread, args=(obj_id, message_text, file_instance))
                thread.start()
