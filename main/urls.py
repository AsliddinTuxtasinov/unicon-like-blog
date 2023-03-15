from django.urls import path
from rest_framework import routers

from .views import (
    MembersViews, InformationServiceViews, InformationServiceDetailViews,
    ResourceDetailView, AnnouncementView, ResourceList,
    ModulsList, ModulDetailView, PartnersList, ContactUsView, StatisticsList
)

router = routers.DefaultRouter()
# router.register(r'create-message', CreateEmailMessages)

urlpatterns = [

    path('member/<str:member_type>', MembersViews.as_view(), name='members-list'),

    path('moduls', ModulsList.as_view(), name='moduls-list'),
    path('moduls/<int:pk>', ModulDetailView.as_view(), name='moduls-detail'),

    path('product/resurslar', ResourceList.as_view(), name='resource-list'),
    path('resource/detail/<int:pk>', ResourceDetailView.as_view(), name='resource-detail'),

    path('xabarlar/<str:type>', AnnouncementView.as_view(), name='announcement-list'),

    # path('services', ServicesListViews.as_view(), name='services-list'),
    # path('services/detail/<int:pk>', ServicesDetailViews.as_view(), name='services-detail'),
    # path('create-message', CreateEmailMessages.as_view(), name='create-message'),

    path('cat/<str:type>', InformationServiceViews.as_view(), name='info-services'),
    path('cat/detail/<int:pk>', InformationServiceDetailViews.as_view(), name='info-services-detail'),

    path('partners', PartnersList.as_view(), name='partners-list'),

    path('contact', ContactUsView.as_view(), name='contact'),

    path('statistics', StatisticsList.as_view(), name='statistics'),

]

urlpatterns += router.urls
