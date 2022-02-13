from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('main', views.main),
    path('teamform', views.teamform),
    path('addteam', views.addTeam),
    path('main/<int:team_id>/edit', views.editteam),
    path('main/<int:team_id>/updateteam', views.updateteam),
    path('main/<int:team_id>/delete', views.deleteteam)
]