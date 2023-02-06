from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import EmailMessages, SubCategories, Categories, Content, ContentImages


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "parent", "is_services"]
    list_filter = ["parent", "is_services"]
    readonly_fields = ["is_services"]


@admin.register(EmailMessages)
class EmailMessagesAdmin(admin.ModelAdmin):
    readonly_fields = ["created_add"]


class ContentImagesInline(admin.TabularInline):
    model = ContentImages
    extra = 1


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ["title", "sub_category", "created_at"]
    inlines = [ContentImagesInline]

    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget()}
    }


admin.site.unregister(Group)
