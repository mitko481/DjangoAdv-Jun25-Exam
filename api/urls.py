from django.urls import path
from . import views
from . import submission_views

urlpatterns = [
    path('quizzes/', views.QuizListAPI.as_view(), name='api_quiz_list'),
    path('quizzes/<slug:slug>/', views.QuizDetailAPI.as_view(), name='api_quiz_detail'),
    path('submissions/', submission_views.UserSubmissionListAPI.as_view(), name='api_user_submissions'),
    path('submissions/<int:pk>/', submission_views.SubmissionDetailAPI.as_view(), name='api_submission_detail'),
]
