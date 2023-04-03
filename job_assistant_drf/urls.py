from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from userapp.views import CustomUserModelViewSet

router = DefaultRouter()
router.register('users', viewset=CustomUserModelViewSet, basename='users')

urlpatterns = [
    path('', include('landingapp.urls')),
    path('admin/', admin.site.urls),
    path('users/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]

handler404 = "landingapp.views.error404"
