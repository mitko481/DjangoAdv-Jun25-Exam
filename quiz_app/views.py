
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, Http404
from .models import Quiz, Question, Choice, Submission, UserAnswer
from .forms import UserRegisterForm
from django.utils import timezone

class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz_app/quiz_list.html'
    context_object_name = 'quizzes'

class QuizDetailView(View):
    def get(self, request, slug):
        quiz = get_object_or_404(Quiz, slug=slug)
        questions = quiz.questions.prefetch_related('choices')
        return render(request, 'quiz_app/quiz_detail.html', {'quiz': quiz, 'questions': questions})

    def post(self, request, slug):
        quiz = get_object_or_404(Quiz, slug=slug)
        questions = quiz.questions.prefetch_related('choices')
        if not request.user.is_authenticated:
            return redirect('login')
        total = questions.count()
        correct = 0
        submission = Submission.objects.create(user=request.user, quiz=quiz, score=0)
        for question in questions:
            selected_id = request.POST.get(f'question_{question.id}')
            if selected_id:
                try:
                    selected_choice = question.choices.get(id=selected_id)
                except Choice.DoesNotExist:
                    continue
                is_correct = selected_choice.is_correct
                UserAnswer.objects.create(
                    submission=submission,
                    question=question,
                    selected_choice=selected_choice,
                    correct=is_correct
                )
                if is_correct:
                    correct += 1
        submission.score = correct
        submission.save()
        return redirect('quiz_result', submission_id=submission.id)

@method_decorator(login_required, name='dispatch')
class QuizResultView(DetailView):
    model = Submission
    template_name = 'quiz_app/results.html'
    context_object_name = 'submission'

    def get_object(self):
        return get_object_or_404(Submission, id=self.kwargs['submission_id'], user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = self.object.answers.select_related('question', 'selected_choice')
        context['quiz'] = self.object.quiz
        return context

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quiz_list')
    else:
        form = UserRegisterForm()
    return render(request, 'quiz_app/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('quiz_list')
    else:
        form = AuthenticationForm()
    return render(request, 'quiz_app/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('quiz_list')

@login_required
def profile(request):
    submissions = request.user.submissions.select_related('quiz').order_by('-timestamp')
    profile = getattr(request.user, 'profile', None)
    return render(request, 'quiz_app/profile.html', {'submissions': submissions, 'profile': profile})

# Custom 404 error handler
def custom_404(request, exception):
    return render(request, 'quiz_app/404.html', status=404)
    return render(request, 'quiz_app/profile.html', {'submissions': submissions})