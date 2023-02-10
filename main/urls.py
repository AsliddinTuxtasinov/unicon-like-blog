from django.urls import path
from rest_framework import routers

from .views import (
    CreateEmailMessages, MembersViews, InformationServiceViews, InformationServiceDetailViews,
    ProductDetailView, ResourceDetailView, AnnouncementView, ServicesListViews, ServicesDetailViews, ResourceList,
    ProductList, PartnersList, ContactUsView
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

    path('cat/<str:type>', InformationServiceViews.as_view(), name='info-services'),
    path('cat/detail/<int:pk>', InformationServiceDetailViews.as_view(), name='info-services-detail'),

    path('partners', PartnersList.as_view(), name='partners-list'),
    path('contact', ContactUsView.as_view(), name='contact'),

]

urlpatterns += router.urls
