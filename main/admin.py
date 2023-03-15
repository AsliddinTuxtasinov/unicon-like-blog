from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.contrib.auth.models import Group

from modeltranslation.admin import TranslationAdmin

from .models import (
    InformationService, ContentAdditionalFiles, Members, Modul,
    Resource, ResourceContent, Announcement, ContactUs, Partners,
    Statistics, Services
)


@admin.register(Members)
class MembersAdmin(TranslationAdmin):
    list_display = ["full_name", "department", ]
    list_filter = ["member_type"]



@admin.register(Modul)
class ModulAdmin(admin.ModelAdmin):
    list_display = ["state_register_number", "name_of_the_legal_entity", "accreditation_date", "valid_status"]


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


# @admin.register(EmailMessages)
# class EmailMessagesAdmin(admin.ModelAdmin):
#     list_display = ["name", "services"]
#     list_filter = ["services"]
#     readonly_fields = ["created_at"]


# InformationService (Axborot xizmatlari)
class ContentFilesInline(admin.TabularInline):
    model = ContentAdditionalFiles
    readonly_fields = ['is_video']
    extra = 1


@admin.register(InformationService)
class InformationServiceAdmin(TranslationAdmin):
    list_display = ["title", "info_cat", "created_at"]
    inlines = [ContentFilesInline]
    readonly_fields = ["views_count"]
    list_filter = ["info_cat"]

    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget()}
    }


admin.site.unregister(Group)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "phone_number", "created_at"]
    readonly_fields = ['created_at']


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Statistics)
class StatisticsAdmin(TranslationAdmin):
    list_display = ["name"]
