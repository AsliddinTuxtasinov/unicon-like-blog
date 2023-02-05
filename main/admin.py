from django.contrib import admin
from .models import EmailMessages, SubCategories, Categories, Content


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "parent"]
    list_filter = ["parent", "is_services"]


@admin.register(EmailMessages)
class EmailMessagesAdmin(admin.ModelAdmin):
    readonly_fields = ["created_add"]


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ["title", "sub_category", "created_at"]
