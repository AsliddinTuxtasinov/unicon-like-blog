from modeltranslation.translator import TranslationOptions, register

from .models import InformationService


@register(InformationService)
class InformationServiceOptions(TranslationOptions):
    fields = ('title', 'content')
