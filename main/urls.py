from django.urls import path
from rest_framework import routers

from .views import (
    CreateEmailMessages, MembersViews, InformationServiceViews, InformationServiceDetailViews,
    ProductDetailView, ResourceDetailView, AnnouncementView, ServicesListViews, ServicesDetailViews, ResourceList,
    ProductList, PartnersList, ContactUsView, StatisticsList, InformationServiceWithVideoViews,
    InformationServiceWithVideoDetailViews
)

router = routers.DefaultRouter()
# router.register(r'create-message', CreateEmailMessages)

urlpatterns = [

    path('member/<str:member_type>', MembersViews.as_view(), name='members-list'),

    path('product/mahsulotlar', ProductList.as_view(), name='product-list'),
    path('product/resurslar', ResourceList.as_view(), name='resource-list'),
    path('product/detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('resource/detail/<int:pk>', ResourceDetailView.as_view(), name='resource-detail'),

    path('xabarlar/<str:type>', AnnouncementView.as_view(), name='announcement-list'),

    path('services', ServicesListViews.as_view(), name='services-list'),
    path('services/detail/<int:pk>', ServicesDetailViews.as_view(), name='services-detail'),
    path('create-message', CreateEmailMessages.as_view(), name='create-message'),

    path('catp/<str:type>', InformationServiceViews.as_view(), name='info-services'),
    path('catp/detail/<int:pk>', InformationServiceDetailViews.as_view(), name='info-services-detail'),
    path('catv/<str:type>', InformationServiceWithVideoViews.as_view(), name='info-services-video'),
    path('catv/detail/<int:pk>', InformationServiceWithVideoDetailViews.as_view(), name='info-services-video-detail'),

    path('partners', PartnersList.as_view(), name='partners-list'),

    path('contact', ContactUsView.as_view(), name='contact'),

    path('statistics', StatisticsList.as_view(), name='statistics'),

]

urlpatterns += router.urls
