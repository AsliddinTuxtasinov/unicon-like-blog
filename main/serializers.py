from .models import EmailMessages, SubCategories, Categories, Content
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


class ContentSerializers(serializers.ModelSerializer):
    subCategories = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = "__all__"

    @staticmethod
    def get_subCategories(obj):
        return SubCategoriesSerializers(obj.sub_category).data


class EmailMessagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmailMessages
        fields = "__all__"
