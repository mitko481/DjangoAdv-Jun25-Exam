from quiz_app.models import Quiz, Question, Choice
from django.contrib.auth import get_user_model

def create_sample_quizzes():
    # Quiz 1
    quiz1 = Quiz.objects.create(title='General Knowledge', slug='general-knowledge', description='A basic general knowledge quiz.')
    q1 = Question.objects.create(quiz=quiz1, text='What is the capital of France?')
    Choice.objects.create(question=q1, text='Paris', is_correct=True)
    Choice.objects.create(question=q1, text='London', is_correct=False)
    Choice.objects.create(question=q1, text='Berlin', is_correct=False)
    q2 = Question.objects.create(quiz=quiz1, text='Which planet is known as the Red Planet?')
    Choice.objects.create(question=q2, text='Mars', is_correct=True)
    Choice.objects.create(question=q2, text='Jupiter', is_correct=False)
    Choice.objects.create(question=q2, text='Venus', is_correct=False)

    # Quiz 2
    quiz2 = Quiz.objects.create(title='Math Quiz', slug='math-quiz', description='A simple math quiz.')
    q3 = Question.objects.create(quiz=quiz2, text='What is 2 + 2?')
    Choice.objects.create(question=q3, text='4', is_correct=True)
    Choice.objects.create(question=q3, text='3', is_correct=False)
    Choice.objects.create(question=q3, text='5', is_correct=False)
    q4 = Question.objects.create(quiz=quiz2, text='What is the square root of 9?')
    Choice.objects.create(question=q4, text='3', is_correct=True)
    Choice.objects.create(question=q4, text='9', is_correct=False)
    Choice.objects.create(question=q4, text='6', is_correct=False)

    print('Sample quizzes created!')

# Usage:
# python manage.py shell
# >>> from quiz_app.sample_quizzes import create_sample_quizzes
# >>> create_sample_quizzes()
