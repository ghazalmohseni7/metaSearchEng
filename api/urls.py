from django.urls import path
from . import views

urlpatterns = [
    path('search/',views.searchAPIView.as_view(),name='search'),
]
