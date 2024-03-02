from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.home_view, name='index'),
    path('activation/', include('users.urls')),
    path('register/', views.register, name='register'),
    path('notes/', views.notes, name='notes'),
    path('notes/<int:pk>/', views.notes_page, name='notes_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('add_note/', views.add_note, name='add_note'),
    path('edit_note/<int:pk>/', views.edit_note, name='edit_note'),
    path('delete_note/<int:pk>/', views.delete_note, name='delete_note'),
    




    path('api/', include(router.urls)),
    path('api/auth', jwt_views.TokenObtainPairView.as_view(),name='API auth'),
    path('api/auth/refresh', jwt_views.TokenRefreshView.as_view(),name='API auth refresh'),
    path('api/notes/', views.api_notes, name='api_notes'),
    path('api/notes/add/', views.api_add_note, name='api_add_note'),
    path('api/notes/edit/<int:pk>/', views.api_edit_note, name='api_edit_note'),
    path('api/notes/delete/<int:pk>/', views.api_delete_note, name='api_delete_note'),
    path('api/notes/details/<int:pk>/', views.api_notes_details, name='api_notes_details'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)