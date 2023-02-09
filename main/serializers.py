from .models import (
    EmailMessages, InformationService, ContentImages, Members, Product, Resource,
    ResourceContent, Announcement, Services
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
    resource = serializers.SerializerMethodField()

    class Meta:
        model = ResourceContent
        fields = "__all__"

    @staticmethod
    def get_resource(obj):
        return ResourceSerializers(obj.resource).data


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

    class Meta:
        model = ContentImages
        fields = "__all__"


class InformationServiceSerializers(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    views_count = serializers.SerializerMethodField()

    class Meta:
        model = InformationService
        fields = "__all__"

    @staticmethod
    def get_images(obj):
        return InformationServiceImagesSerializers(obj.content_images.all(), many=True).data

    @staticmethod
    def get_views_count(obj):
        return obj.content_views_count.count()


class EmailMessagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmailMessages
        fields = "__all__"
