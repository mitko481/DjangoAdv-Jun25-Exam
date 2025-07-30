
# Trivio
This is a trivia application built with Django that includes user authentication, quiz management, result tracking, REST API, user profiles, and custom middleware.

## Features
- User registration and authentication (with custom validation)
- Create and manage quizzes
- Answer questions and submit responses
- View results and feedback on answers
- Profile page with quiz history, bio, and avatar
- REST API for quizzes and user submissions (Django REST Framework)
- Custom request logging middleware
- Admin interface for managing quizzes

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd quiz_project
   ```
2. Create a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or
   source .venv/bin/activate  # On Linux/Mac
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   pip install djangorestframework Pillow
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```

## UI/UX Enhancements
Trivio includes the following interactive and visual improvements:
- **Confetti Animation:** When you achieve a perfect score on a quiz, a confetti effect will celebrate your success on the results page.
- **Animated Score Reveal:** Your score is smoothly revealed with a counting animation after submitting a quiz.
- **Ripple & Hover Effects:** All buttons feature a modern ripple effect and animated hover for better feedback.
- **Animated Question Cards:** Questions fade in with a staggered animation for a more dynamic quiz experience.
- **Progress Bar:** A progress bar at the top of each quiz animates as you answer questions.

All enhancements use lightweight JavaScript and CSS, and require no extra setup. For the confetti effect, the app uses the [canvas-confetti](https://www.npmjs.com/package/canvas-confetti) library via CDN.

## Usage
- Navigate to `http://127.0.0.1:8000/` to access the application.
- Register a new user or log in with existing credentials.
- View available quizzes and participate in them.
- After submitting a quiz, view your results.
