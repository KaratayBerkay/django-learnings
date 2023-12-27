"""
URL configuration for mini_project project.
"""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
# from user_service.views import CategoryViewSet

router = DefaultRouter()
# router.register(r"question", CategoryViewSet)


urlpatterns = [
    path("user_service/", include("user_service.urls")),
    path("admin/", admin.site.urls),
    path('api_schema/', get_schema_view(title='API Schema', description='Guide for the REST API'), name='api_schema'),
    path("swagger-ui/", TemplateView.as_view(
        template_name="swagger-ui.html",  extra_context={"schema_url": "api_schema"}), name="swagger-ui"
         ),
]
