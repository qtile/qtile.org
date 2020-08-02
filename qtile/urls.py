from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('download/', views.Download.as_view(), name='download'),
    path('screenshots/', views.Screenshots.as_view(), name='screenshots'),
    path('videos/', views.Videos.as_view(), name='videos'),
]
