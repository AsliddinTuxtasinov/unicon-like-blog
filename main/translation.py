from modeltranslation.translator import TranslationOptions, register

from .models import (
    InformationService, Members, Product, Resource, ResourceContent, Announcement, Services, Statistics
)


@register(Members)
class MembersOptions(TranslationOptions):
    fields = ('full_name', 'department', 'workday')


@register(Product)
class ProductOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Resource)
class ResourceOptions(TranslationOptions):
    fields = ('title', 'short_desc')


@register(ResourceContent)
class ResourceContentOptions(TranslationOptions):
    fields = ('name', 'short_desc')


@register(Announcement)
class AnnouncementOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Services)
class ServicesOptions(TranslationOptions):
    fields = ('name', 'title', 'content')


@register(InformationService)
class InformationServiceOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Statistics)
class StatisticsOptions(TranslationOptions):
    fields = ('name',)
