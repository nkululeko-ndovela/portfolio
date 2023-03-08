from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/map/', views.map_view,name='profiles',
    path('profile/edit/', views.edit_profile_view,name='edit_profile_view'),
]