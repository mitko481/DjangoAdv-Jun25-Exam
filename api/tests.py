from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from quiz_app.models import Quiz
from rest_framework import status

class QuizAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='apitest', password='testpass', email='apitest@example.com')
        self.quiz = Quiz.objects.create(title='API Quiz', slug='api-quiz', description='API test quiz')

    def test_quiz_list_api(self):
        response = self.client.get('/api/quizzes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('API Quiz' in str(response.data))

    def test_user_submissions_api_auth_required(self):
        response = self.client.get('/api/submissions/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.login(username='apitest', password='testpass')
        response = self.client.get('/api/submissions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
