from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>', views.userProfile, name="user-profile"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('edit-user/', views.updateUser, name="edit-profile"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('topics/', views.topicsPage, name="topics"),
    path('recent-activities/', views.recentActivities, name="recent-activities"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)