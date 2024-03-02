from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views.activation import reset_token_view, activate_user

app_name = 'activation'

urlpatterns = [
    path('activate/', activate_user, name='activate'),
    path('reset_token/', reset_token_view, name='reset_token'),
]