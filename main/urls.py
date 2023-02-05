from django.urls import path
from rest_framework import routers

from .views import CreateEmailMessages, GetCategories, ContentList

router = routers.DefaultRouter()
# router.register(r'create-message', CreateEmailMessages)

urlpatterns = [
    path('create-message', CreateEmailMessages.as_view(), name='create-message'),
    path('categories', GetCategories.as_view(), name='categories'),
    path('contents', ContentList.as_view(), name='contents-list'),
]

urlpatterns += router.urls
