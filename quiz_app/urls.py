from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuizListView.as_view(), name='quiz_list'),
    path('quiz/<slug:slug>/', views.QuizDetailView.as_view(), name='quiz_detail'),
    path('result/<int:submission_id>/', views.QuizResultView.as_view(), name='quiz_result'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]