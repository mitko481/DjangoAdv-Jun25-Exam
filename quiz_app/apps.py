from django.apps import AppConfig

class QuizAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quiz_app'

    def ready(self):
        from django.contrib.auth.models import User
        from django.db.models.signals import post_save
        from .user_profile import UserProfile
        def create_user_profile(sender, instance, created, **kwargs):
            if created:
                UserProfile.objects.create(user=instance)
        post_save.connect(create_user_profile, sender=User)