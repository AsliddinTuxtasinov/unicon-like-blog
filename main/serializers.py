from .models import (
    InformationService, ContentAdditionalFiles,
    Members, Modul, Resource, ResourceContent, Announcement, ContactUs, Partners, Statistics,
)
from rest_framework import serializers


class MembersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = "__all__"


class ModulSerializers(serializers.ModelSerializer):

    class Meta:
        model = Modul
        fields = "__all__"


class ResourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"


class ResourceContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = ResourceContent
        fields = "__all__"


class ResourceDetailSerializers(serializers.ModelSerializer):
    resources = serializers.SerializerMethodField()

    class Meta:
        model = Resource
        fields = "__all__"

    @staticmethod
    def get_resources(obj):
        return ResourceContentSerializers(obj.resource_content.all(), many=True).data


class AnnouncementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"


# class ServicesSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Services
#         # fields = ["id", "name", "title", "content", "created_at"]
#         exclude = ["email"]


# InformationService
class InformationServiceFilesSerializers(serializers.ModelSerializer):
    is_video = serializers.BooleanField()

    class Meta:
        model = ContentAdditionalFiles
        fields = "__all__"


class InformationServiceSerializers(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()

    class Meta:
        model = InformationService
        fields = "__all__"

    @staticmethod
    def get_files(obj):
        return InformationServiceFilesSerializers(obj.content_files.all(), many=True).data


# class EmailMessagesSerializers(serializers.ModelSerializer):
#     file = serializers.FileField(required=False)

#     class Meta:
#         model = EmailMessages
#         fields = "__all__"


class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class PartnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = "__all__"


class StatisticsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = "__all__"
