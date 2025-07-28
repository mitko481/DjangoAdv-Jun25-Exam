
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

## Project Structure

```
quiz_project
├── quiz_app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── user_profile.py
│   ├── middleware.py
│   └── templates
│       └── quiz_app
│           ├── base.html
│           ├── quiz_list.html
│           ├── quiz_detail.html
│           ├── registration.html
│           ├── login.html
│           ├── logout.html
│           ├── results.html
│           ├── profile.html
│           └── 404.html
├── api
│   ├── serializers.py
│   ├── submission_serializers.py
│   ├── views.py
│   ├── submission_views.py
│   ├── urls.py
│   └── tests.py
├── quiz_project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

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

## Adding Quizzes, Questions, and Answers via the Admin Page

To add a new quiz (such as a "Gaming" quiz, for example) and ensure questions and correct answers are set up properly in Trivio, follow these steps:

1. **Log in to the Django admin page**  
   Go to `/admin/` and log in with your superuser account.

2. **Add a new Quiz**  
   - Click on "Quizzes".
   - Click "Add Quiz".
   - Enter the quiz title (e.g., "Gaming"), a unique slug (e.g., "gaming"), and an optional description.
   - Save the quiz.

3. **Add Questions to the Quiz**  
   - After saving, you can add questions directly from the Quiz change page or go to "Questions" in the admin sidebar.
   - Click "Add Question".
   - Select the quiz you just created from the dropdown (e.g., "Gaming").
   - Enter the question text (e.g., "What year was the first PlayStation released?").
   - Save the question.

4. **Add Choices and Mark the Correct Answer**  
   - After saving a question, you can add choices (answers) for it.
   - For each choice, enter the answer text (e.g., "1994", "1996", "2000").
   - For the correct answer, check the "Is correct" box.
   - You can add multiple choices, but only one should be marked as correct for standard multiple-choice questions.
   - Save each choice.

5. **Repeat for More Questions**  
   - Add as many questions and choices as needed for your quiz.

6. **Verify**  
   - Make sure each question has at least one correct answer marked.
   - Each question should belong to the correct quiz (e.g., "Gaming").

---

   OPTIONAL: When installed, add to PATH to prevent any problems from occuring (steps should be provided when you run ```pip install django```).


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



## REST API
- List quizzes: `GET /api/quizzes/`
- Quiz detail: `GET /api/quizzes/<slug>/`
- List your submissions: `GET /api/submissions/` (requires login)
- Submission detail: `GET /api/submissions/<id>/` (requires login)

## User Profile
- Each user has a profile with bio and avatar (image upload).
- Profile is auto-created on registration.

## Middleware
- All requests are logged by custom middleware in `quiz_app/middleware.py`.

## Testing
- Run API tests with:
  ```
  python manage.py test api
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