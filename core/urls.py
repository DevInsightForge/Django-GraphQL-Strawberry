"""core URL Configuration

"""
from django.contrib import admin
from strawberry.django.views import GraphQLView
from django.urls import path
from core.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GraphQLView.as_view(schema=schema)),
]
