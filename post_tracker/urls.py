from django.urls import path
from . import views

app_name = "post_tracker"

urlpatterns = [
    path('', views.track_page, name='track_page'),
    path('get/', views.search_track, name='search_track'),
]
