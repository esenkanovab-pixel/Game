from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # players
    path('players/', views.players_list, name='players_list'),
    path('players/new/', views.player_create, name='player_create'),
    path('players/<int:pk>/edit/', views.player_edit, name='player_edit'),
    path('players/<int:pk>/delete/', views.player_delete, name='player_delete'),
    # questions
    path('questions/', views.questions_list, name='questions_list'),
    path('questions/new/', views.question_create, name='question_create'),
    path('questions/<int:pk>/edit/', views.question_edit, name='question_edit'),
    path('questions/<int:pk>/delete/', views.question_delete, name='question_delete'),
    # sessions
    path('sessions/', views.sessions_list, name='sessions_list'),
    path('sessions/new/', views.session_create, name='session_create'),
    path('sessions/<int:pk>/', views.session_view, name='session_view'),
    path('sessions/<int:pk>/play/', views.play_session, name='play_session'),
    # results
    path('results/', views.results_list, name='results_list'),
]
