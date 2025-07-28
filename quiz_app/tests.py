from django.test import TestCase
from .models import Quiz, Question, Choice, Submission, UserAnswer
from django.contrib.auth.models import User

class QuizModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.quiz = Quiz.objects.create(title='Sample Quiz', slug='sample-quiz', description='A sample quiz for testing.')
        self.question = Question.objects.create(quiz=self.quiz, text='What is the capital of France?', question_type='text')
        self.choice = Choice.objects.create(question=self.question, text='Paris', is_correct=True)

    def test_quiz_creation(self):
        self.assertEqual(self.quiz.title, 'Sample Quiz')
        self.assertEqual(self.quiz.slug, 'sample-quiz')
        self.assertEqual(self.quiz.description, 'A sample quiz for testing.')

    def test_question_creation(self):
        self.assertEqual(self.question.text, 'What is the capital of France?')
        self.assertEqual(self.question.quiz, self.quiz)

    def test_choice_creation(self):
        self.assertEqual(self.choice.text, 'Paris')
        self.assertTrue(self.choice.is_correct)

class SubmissionModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.quiz = Quiz.objects.create(title='Sample Quiz', slug='sample-quiz', description='A sample quiz for testing.')
        self.submission = Submission.objects.create(user=self.user, quiz=self.quiz, score=10)

    def test_submission_creation(self):
        self.assertEqual(self.submission.user, self.user)
        self.assertEqual(self.submission.quiz, self.quiz)
        self.assertEqual(self.submission.score, 10)

class UserAnswerModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.quiz = Quiz.objects.create(title='Sample Quiz', slug='sample-quiz', description='A sample quiz for testing.')
        self.question = Question.objects.create(quiz=self.quiz, text='What is the capital of France?', question_type='text')
        self.choice = Choice.objects.create(question=self.question, text='Paris', is_correct=True)
        self.submission = Submission.objects.create(user=self.user, quiz=self.quiz, score=10)
        self.user_answer = UserAnswer.objects.create(submission=self.submission, question=self.question, selected_choice=self.choice, correct=True)

    def test_user_answer_creation(self):
        self.assertEqual(self.user_answer.submission, self.submission)
        self.assertEqual(self.user_answer.question, self.question)
        self.assertEqual(self.user_answer.selected_choice, self.choice)
        self.assertTrue(self.user_answer.correct)