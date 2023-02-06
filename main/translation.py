from modeltranslation.translator import TranslationOptions, register

from .models import Content


@register(Content)
class ContentOptions(TranslationOptions):
    fields = ('title', 'content')
