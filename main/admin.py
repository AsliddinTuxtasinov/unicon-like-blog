from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.contrib.auth.models import Group

from modeltranslation.admin import TranslationAdmin

from .models import (
    EmailMessages, InformationService, ContentImages, Members, Product,
    Resource, ResourceContent, Announcement, Services, InformationServiceContentViewsModel
)


@admin.register(Members)
class MembersAdmin(TranslationAdmin):
    list_display = ["full_name", "department", ]
    list_filter = ["member_type"]


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ["title"]


@admin.register(Resource)
class ResourceAdmin(TranslationAdmin):
    list_display = ["title"]


@admin.register(ResourceContent)
class ResourceContentAdmin(TranslationAdmin):
    list_display = ["name", "resource"]


@admin.register(Announcement)
class AnnouncementAdmin(TranslationAdmin):
    list_display = ["title", "announcement_status", "status_type"]


@admin.register(Services)
class ServicesAdmin(TranslationAdmin):
    list_display = ["name"]


@admin.register(EmailMessages)
class EmailMessagesAdmin(admin.ModelAdmin):
    list_display = ["title", "services", "name_organization", "full_name"]
    list_filter = ["services"]
    readonly_fields = ["created_add"]


class ContentImagesInline(admin.TabularInline):
    model = ContentImages
    extra = 1


@admin.register(InformationService)
class InformationServiceAdmin(TranslationAdmin):
    list_display = ["title", "created_at"]
    inlines = [ContentImagesInline]
    readonly_fields = ["views_count"]

    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget()}
    }


admin.site.unregister(Group)


# @admin.register(InformationServiceContentViewsModel)
# class InformationServiceContentViewsModelAdmin(admin.ModelAdmin):
#     pass
