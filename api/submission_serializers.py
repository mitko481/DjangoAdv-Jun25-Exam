from rest_framework import serializers
from quiz_app.models import Submission, UserAnswer, Quiz, Question, Choice

class UserAnswerSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='question.text', read_only=True)
    selected_choice = serializers.CharField(source='selected_choice.text', read_only=True)
    class Meta:
        model = UserAnswer
        fields = ['question', 'selected_choice', 'correct']

class SubmissionSerializer(serializers.ModelSerializer):
    quiz = serializers.CharField(source='quiz.title', read_only=True)
    answers = UserAnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Submission
        fields = ['id', 'quiz', 'score', 'timestamp', 'answers']
