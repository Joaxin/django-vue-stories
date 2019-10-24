from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import MessageViewSet
from rest_framework.authtoken import views

app_name = 'lime'


router = routers.DefaultRouter()
router.register('messages', MessageViewSet)


urlpatterns = [
     path('', include(router.urls)),
     path('admin/', admin.site.urls),
]
