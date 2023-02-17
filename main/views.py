from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework import response, status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import (
    EmailMessages, Members, Resource, Announcement, Services, InformationService,
    Partners, ContactUs, Statistics, Modul
)
from .serializers import (
    EmailMessagesSerializers, MembersSerializers, InformationServiceSerializers,
    ResourceSerializers, AnnouncementSerializers, ServicesSerializers,
    PartnersSerializers, ContactUsSerializers, ResourceDetailSerializers, StatisticsSerializers, ModulSerializers,
)
from .utils import error_response_404


@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=["member"],
    operation_summary="Member(rahbariyat, ilmiykengash, jamoa) larni royxatini olish",
    operation_description="member_type = ['rahbariyat', 'ilmiykengash', 'team'] -> shulardan biri bo'lishi mumkin",
    operation_id="members-list",
    responses={'200': "Response json ko'rinishida bo'ladi va memberlar listi keladi"}
))
class MembersViews(APIView):
    # Define the serializer class to be used for serializing the data
    serializer_class = MembersSerializers

    # Map incoming member type to string representation
    member_types = {
        "rahbariyat": 'RT',
        "ilmiykengash": 'IK',
        "team": 'BJ',
    }

    def get(self, *args, **kwargs):
        # Get the member_type from URL parameters
        member_type = self.member_types.get(kwargs.get("member_type", "").lower(), None)

        # If the incoming member_type is not found in the map, return a 404 error
        if member_type is None:
            error_response_404()

        # Filter the Members objects using the member_type
        members_obj = Members.objects.filter(member_type=member_type)

        # Serialize the filtered queryset using the MembersSerializers serializer
        serializer = self.serializer_class(members_obj, many=True)

        # Return the serialized data as a JSON response with a 200 OK status
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=["Moduls"],
    operation_summary="Moduls (bo'limlar) royxatini olish",
    operation_description="",
    operation_id="moduls-list",
    responses={'200': "Response json ko'rinishida bo'ladi va maxsulotlar royxati keladi"}
))
class ModulsList(ListAPIView):
    queryset = Modul.objects.all()
    serializer_class = ModulSerializers
    permission_classes = [AllowAny]


@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=["Moduls"],
    operation_summary="Moduls (bo'limlar) id orqali detail qismiga kirish",
    operation_description="id -> Modul (bo'lim) id si, uni maxsulotlar ro'yxatidan olinadi",
    operation_id="moduls-detail",
    responses={'200': "Response json ko'rinishida bo'ladi va maxsulot detail keladi"}
))
class ModulDetailView(RetrieveAPIView):
    queryset = Modul.objects.all()
    serializer_class = ModulSerializers
    permission_classes = [AllowAny]


@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=["resource"],
    operation_summary="Resurslar royxatini olish",
    operation_description="",
    operation_id="resource-list",
    responses={'200': "Response json ko'rinishida bo'ladi va resurslar ro'yxati keladi"}
))
class ResourceList(ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializers
    permission_classes = [AllowAny]


@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=["resource"],
    operation_summary="Resource id orqali resurslar ichidagi resurlar ro'yxatini filter qilish",
    operation_description="id -> resurs id si, uni resurslar ro'yxatidan olinadi",
    operation_id="resource-detail",
    responses={'200': "Response json ko'rinishida bo'ladi va filterlangan resurslar ro'yxati keladi"}
))
class ResourceDetailView(APIView):
    # Define the serializer class to use for this view
    serializer_class = ResourceDetailSerializers

    def get(self, *args, **kwargs):
        # Retrieve the primary key (pk) value from the URL kwargs
        pk = kwargs.get("pk", None)

        # If the pk value is None, return a 404 NOT FOUND response
        if pk is None:
            error_response_404()

        # Use the resource__resource_content__pk look-up to filter
        # the ResourceContent objects related to the given pk
        resource_obj = Resource.objects.filter(pk=pk)

        # Serialize the filtered ResourceContent objects using the defined serializer class
        serializer = self.serializer_class(resource_obj, many=True)

        # Return the serialized data as a JSON response with a 200 OK status
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=["Announcement"],
    operation_summary="Announcement type orqali filter qiladi va filterlangan e'lonlar ro'yxatini qaytaradi",
    operation_description="type = ['konkurslar', 'takliflar'] bo'lishi mumkin",
    operation_id="announcement-list",
    responses={'200': "Response json ko'rinishida bo'ladi va filterlangan ro'yxati keladi"}
))
class AnnouncementView(APIView):
    # Define the serializer class to be used for this view
    serializer_class = AnnouncementSerializers

    # Create a dictionary mapping string values in the URL to constants in the model
    types_api = {
        'konkurslar': 'CS',
        'takliflar': 'IK',
    }

    def get(self, *args, **kwargs):
        # Get the value of the "type" argument from the URL
        # Look up the corresponding constant value in the model based on the string argument
        type_api = self.types_api.get(kwargs.get("type", "").lower(), None)
        # If the argument is not recognized, return a 404 error response
        if type_api is None:
            error_response_404()

        # Filter the announcements based on the provided "type" argument
        announcement_obj = Announcement.objects.filter(announcement_status=type_api)

        # Use the defined serializer class to serialize the filtered announcements
        serializer = self.serializer_class(announcement_obj, many=True)

        # Return the serialized data in a 200 OK response
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=["Services"],
    operation_summary="Services(Xizmatlar) larni ro'yxatini olish",
    operation_description="",
    operation_id="services-list",
    responses={'200': "Response json ko'rinishida bo'ladi va services ro'yxati keladi"}
))
class ServicesListViews(ListAPIView):
    serializer_class = ServicesSerializers
    queryset = Services.objects.all()
    permission_classes = [AllowAny]


@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=["Services"],
    operation_summary="Services(Xizmatlar) detail olish",
    operation_description="id - bu orqali service ni oladi",
    operation_id="services-detail",
    responses={'200': "Response json ko'rinishida bo'ladi va services ro'yxati keladi"}
))
class ServicesDetailViews(RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    permission_classes = [AllowAny]


@method_decorator(name='post', decorator=swagger_auto_schema(
    tags=["Services"],
    operation_summary="Services(Xizmatlar) ga message qoldirish",
    operation_description="Bu message service ga biriktirilgan emailga jo'natiladi",
    operation_id="create-message",
    responses={'200': "Response json ko'rinishida bo'ladi va services ro'yxati keladi"}
))
class CreateEmailMessages(CreateAPIView):
    queryset = EmailMessages.objects.all()
    serializer_class = EmailMessagesSerializers
    permission_classes = [AllowAny]


# InformationService (Axborot xizmatlari)
@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=["Information Service (Axborot Xizmati)"],
    operation_summary="Information Service (Axborot Xizmati) ro'yxatini olish [only photo items section]",
    operation_description="type=['yangiliklar', 'foto', 'memorandum', 'oav', 'video'] - shulardan biri bo'lishi mumkin va bu orqali objects ni filterlab beradi",
    operation_id="info-services",
    responses={
        '200': "Response json ko'rinishida bo'ladi va object(Information Service [Axborot Xizmati]) ro'yxati keladi"}
))
class InformationServiceViews(APIView):
    # Define the serializer class to be used for this view
    serializer_class = InformationServiceSerializers

    # Create a dictionary mapping string values in the URL to constants in the model
    types_api = {
        'yangiliklar': 'NS',
        'foto': 'PR',
        'memorandum': 'MM',
        'oav': 'OU',
        'video': 'VR',
    }

    def get(self, *args, **kwargs):
        # Get the value of the "type" argument from the URL
        # Look up the corresponding constant value in the model based on the string argument
        type_api = self.types_api.get(kwargs.get("type", "").lower(), None)
        # If the argument is not recognized, return a 404 error response
        if type_api is None:
            error_response_404()

        # Filter the announcements based on the provided "type" argument
        obj = InformationService.objects.filter(info_cat=type_api)

        # Use the defined serializer class to serialize the filtered announcements
        serializer = self.serializer_class(obj, many=True)

        # Return the serialized data in a 200 OK response
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=["Information Service (Axborot Xizmati)"],
    operation_summary="Information Service (Axborot Xizmati) [only photo items] detail olish",
    operation_description="id - bu orqali objects ni detail data sini oladi",
    operation_id="info-services-detail",
    responses={
        '200': "Response json ko'rinishida bo'ladi va object(Information Service [Axborot Xizmati]) detail keladi"}
))
class InformationServiceDetailViews(RetrieveAPIView):
    serializer_class = InformationServiceSerializers
    queryset = InformationService.objects.all()
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Check if the user has viewed this post before
        viewed_posts = request.session.get('viewed_posts', [])
        print(viewed_posts)

        if instance.id not in viewed_posts:
            # User has not viewed this post before, so increment the view count
            instance.views_count += 1
            instance.save()

            # Add the post ID to the viewed_posts session
            viewed_posts.append(instance.id)
            request.session['viewed_posts'] = viewed_posts

        # User has already viewed this post, so don't increment the view count
        return response.Response(serializer.data)


class PartnersList(ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializers
    permission_classes = [AllowAny]


class StatisticsList(ListAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializers
    permission_classes = [AllowAny]


class ContactUsView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializers
    permission_classes = [AllowAny]
