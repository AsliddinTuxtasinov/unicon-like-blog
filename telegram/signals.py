import asyncio
import threading
from aiogram import types

from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import EmailMessages, ContactUs
from telegram.bot import bot, dp
from telegram.models import TelegramBot
from aiogram.utils.exceptions import BotKicked

# Create a lock to control access to the function
lock = threading.Lock()

chat_ids = TelegramBot.objects.all()


async def send_message_to_telegram_bot(obj_id, message_text, file):
    with lock:
        # Try to send a message and a document to the chat
        try:
            # Send a message to the chat using the `send_message` method of the bot object.
            # The `chat_id` argument specifies the chat to send the message to, and the `text` argument
            # specifies the text of the message. The `parse_mode` argument specifies the parse mode
            # to use when sending the message. In this case, it is set to `types.ParseMode.HTML`.
            sent_message = await bot.send_message(
                chat_id=obj_id.chat_id, text=message_text,
                parse_mode=types.ParseMode.HTML
            )
            if file is not None:
                # Send a document to the chat using the `send_document` method of the bot object.
                # The `chat_id` argument specifies the chat to send the document to, and the `document`
                # argument specifies the file to be sent. The `reply_to_message_id` argument specifies the
                # message that the document should be sent in reply to, in this case the message sent earlier.
                await bot.send_document(
                    chat_id=obj_id.chat_id, document=open(file, 'rb'),
                    reply_to_message_id=sent_message.message_id
                )

        # Catch the BotKicked exception and print an error message
        except BotKicked as e:
            # Handle the exception here
            print("The bot was kicked from the group chat due to the following error:")
            print(e)


def send_message_in_thread(obj_id, message_text, file_instance=None):
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


@receiver(post_save, sender=ContactUs)
def send_messege_on_contact_creation(sender, instance, created, **kwargs):
    if created:
        message_text = f"<b>F.I.SH/Tashkilot nomi: {instance.full_name}</b>\n" \
                       f"<b>E-mail: {instance.email}</b>\n" \
                       f"<b>Tel: {instance.phone_number}</b>\n" \
                       f"<b>Xabar: {instance.message}</b>\n" \
                       f"<b>Yuborilgan vaqti: </b>{instance.created_add}"

        if chat_ids:
            for obj_id in chat_ids:
                thread = threading.Thread(target=send_message_in_thread, args=(obj_id, message_text))
                thread.start()
