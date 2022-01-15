from django.urls import path

from .views import Cowrywise

urlpatterns = [
    # local app routes
    path('', Cowrywise.as_view(), name='cowrywise')
]
