from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from .models import EmailMessages, Categories, Content
from .serializers import EmailMessagesSerializers, CategoriesSerializers, ContentSerializers


class CreateEmailMessages(CreateAPIView):
    queryset = EmailMessages.objects.all()
    serializer_class = EmailMessagesSerializers
    permission_classes = [AllowAny]


class GetCategories(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers
    permission_classes = [AllowAny]


class ContentList(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializers
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["sub_category"]
