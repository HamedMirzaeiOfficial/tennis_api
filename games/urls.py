from django.urls import path
from . import views

urlpatterns = [
    path('nationalities/', views.NationalityList.as_view(), name=views.NationalityList.name),
    path('nationalities/<int:pk>/', views.NationalityDetail.as_view(), name=views.NationalityDetail.name),
    path('players/', views.PlayerList.as_view(), name=views.PlayerList.name),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name=views.PlayerDetail.name),
    path('competitions/', views.CompetitionList.as_view(), name=views.CompetitionList.name),
    path('competitions/<int:pk>/', views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name)
]
