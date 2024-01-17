from django.shortcuts import render
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Proyectos API",
        default_version='v1',
        description="API para gestionar proyectos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="joshuexd1@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)