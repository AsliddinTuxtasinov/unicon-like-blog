from .models import EmailMessages, SubCategories, Categories, Content, ContentImages
from rest_framework import serializers


class SubCategoriesSerializers(serializers.ModelSerializer):

    class Meta:
        model = SubCategories
        fields = "__all__"


class CategoriesSerializers(serializers.ModelSerializer):
    subCategories = serializers.SerializerMethodField()

    class Meta:
        model = Categories
        fields = "__all__"

    @staticmethod
    def get_subCategories(obj):
        return SubCategoriesSerializers(obj.parent_category.all(), many=True).data


class ContentImagesSerializers(serializers.ModelSerializer):

    class Meta:
        model = ContentImages
        fields = "__all__"


class ContentSerializers(serializers.ModelSerializer):
    subCategories = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = "__all__"

    @staticmethod
    def get_subCategories(obj):
        return SubCategoriesSerializers(obj.sub_category).data

    @staticmethod
    def get_images(obj):
        return ContentImagesSerializers(obj.content_images.all(), many=True).data


class EmailMessagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmailMessages
        fields = "__all__"
