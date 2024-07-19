from django.urls import path  # Powers URL pattern

from .views import home_page_view  # Importing home_page_view from views.py

urlpatterns = [
    path("", home_page_view),
]
