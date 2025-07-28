
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz_app.urls')),
    path('api/', include('api.urls')),
]

# Custom error handlers
handler404 = 'quiz_app.views.custom_404'