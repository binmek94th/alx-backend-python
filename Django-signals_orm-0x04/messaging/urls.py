from django.urls import path

from messaging.views import UserAPiView

urlpatterns = [
    path('user/', UserAPiView.as_view(), name='user-api'),
]