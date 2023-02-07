from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework import response, status, validators
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import (
    EmailMessages, Members, Product, Resource, ResourceContent, Announcement, Services, InformationService
)
from .serializers import (
    EmailMessagesSerializers, MembersSerializers, InformationServiceSerializers,
    ProductSerializers, ResourceSerializers, ResourceContentSerializers, AnnouncementSerializers, ServicesSerializers
)
from .utils import error_response_404


class MembersViews(APIView):
    # Define the serializer class to be used for serializing the data
    serializer_class = MembersSerializers

    # Map incoming member type to string representation
    member_types = {
        "rahbariyat": Members.MembersCat.LEADERSHIP,
        "ilmiykengash": Members.MembersCat.SCIENTIFIC_COUNCIL,
        "team": Members.MembersCat.OUR_TEAM,
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


class ProductOrResourceList(APIView):
    # A map between the incoming type parameter value and the type of object
    # we want to retrieve from the database
    types_api = {
        'mahsulotlar': True,
        'resurslar': False,
    }

    def get(self, *args, **kwargs):
        # Retrieve the value of the "type" parameter from the URL and convert it to lowercase
        type_api = self.types_api.get(kwargs.get("type", "").lower(), None)

        # If the type is not found in the map, return a 404 error
        if type_api is None:
            error_response_404()

        # If type_api is True, retrieve all Product objects from the database and serialize them
        if type_api:
            serializer = ProductSerializers(Product.objects.all(), many=True)
        # If type_api is False, retrieve all Resource objects from the database and serialize them
        else:
            serializer = ResourceSerializers(Resource.objects.all(), many=True)

        # Return the serialized data as a JSON response with a 200 OK status
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [AllowAny]


class ResourceDetailView(APIView):
    # Define the serializer class to use for this view
    serializer_class = ResourceContentSerializers

    def get(self, *args, **kwargs):
        # Retrieve the primary key (pk) value from the URL kwargs
        pk = kwargs.get("pk", None)

        # If the pk value is None, return a 404 NOT FOUND response
        if pk is None:
            error_response_404()

        # Use the resource__resource_content__pk look-up to filter
        # the ResourceContent objects related to the given pk
        resource_obj = ResourceContent.objects.filter(resource__resource_content__pk=pk)

        # Serialize the filtered ResourceContent objects using the defined serializer class
        serializer = self.serializer_class(resource_obj, many=True)

        # Return the serialized data as a JSON response with a 200 OK status
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


class AnnouncementView(APIView):
    # Define the serializer class to be used for this view
    serializer_class = AnnouncementSerializers

    # Create a dictionary mapping string values in the URL to constants in the model
    types_api = {
        'konkurslar': Announcement.AnnouncementCat.COMPETITIONS,
        'takliflar': Announcement.AnnouncementCat.SELECTION_OF_PROPOSALS,
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


class ServicesListViews(ListAPIView):
    serializer_class = ServicesSerializers
    queryset = Services.objects.all()
    permission_classes = [AllowAny]


class ServicesDetailViews(RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    permission_classes = [AllowAny]


class CreateEmailMessages(CreateAPIView):
    queryset = EmailMessages.objects.all()
    serializer_class = EmailMessagesSerializers
    permission_classes = [AllowAny]


class InformationServiceViews(APIView):
    # Define the serializer class to be used for this view
    serializer_class = InformationServiceSerializers

    # Create a dictionary mapping string values in the URL to constants in the model
    types_api = {
        'yangiliklar': InformationService.InformationServiceCat.NEWS,
        'foto': InformationService.InformationServiceCat.PHOTO_REPORT,
        'video': InformationService.InformationServiceCat.VIDEO_REPORT,
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


class InformationServiceDetailViews(RetrieveAPIView):
    serializer_class = InformationServiceSerializers
    queryset = InformationService.objects.all()
    permission_classes = [AllowAny]
