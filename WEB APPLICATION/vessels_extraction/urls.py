from django.urls import path
from vessels_extraction import views as vessels_views

urlpatterns = [
    path('', vessels_views.vessels_segment, name="vessels_segment"),
]