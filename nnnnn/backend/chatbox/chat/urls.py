from django.urls import path, re_path, include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('register/', UserService.as_view(), name='userlist'),
    path('login/<int:pk>/', UserDetail.as_view(), name='userdetail'),
    path('api/schema/',SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]