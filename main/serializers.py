from .models import (
    EmailMessages, InformationService, ContentAdditionalFiles, Members, Product, Resource,
    ResourceContent, Announcement, Services, ContactUs, Partners, Statistics
)
from rest_framework import serializers


class MembersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
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


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        # fields = ["id", "name", "title", "content", "created_at"]
        exclude = ["email"]


class InformationServiceImagesSerializers(serializers.ModelSerializer):
    is_video = serializers.BooleanField()

    class Meta:
        model = ContentAdditionalFiles
        fields = "__all__"


class InformationServiceSerializers(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()
    views_count = serializers.SerializerMethodField()

    class Meta:
        model = InformationService
        fields = "__all__"

    @staticmethod
    def get_files(obj):
        return InformationServiceImagesSerializers(obj.content_images.all(), many=True).data

    @staticmethod
    def get_views_count(obj):
        return obj.content_views_count.count()


class EmailMessagesSerializers(serializers.ModelSerializer):
    file = serializers.FileField(required=False)

    class Meta:
        model = EmailMessages
        fields = "__all__"


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
