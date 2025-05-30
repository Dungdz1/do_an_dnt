from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('users/', UserCreateViews.as_view(), name='users-list-create'),
    path('users/<str:email>/', UserUpdateViews.as_view(), name='users-detail'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
