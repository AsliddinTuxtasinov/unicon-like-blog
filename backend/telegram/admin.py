from django.contrib import admin

from telegram.models import TelegramBot


@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
    list_display = ["chat_id", "name"]
