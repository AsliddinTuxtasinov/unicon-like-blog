from django.db import models


class TelegramBot(models.Model):
    chat_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.chat_id)
