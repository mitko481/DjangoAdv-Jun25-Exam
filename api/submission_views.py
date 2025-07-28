from rest_framework import generics, permissions
from quiz_app.models import Submission
from .submission_serializers import SubmissionSerializer

class UserSubmissionListAPI(generics.ListAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user).order_by('-timestamp')

class SubmissionDetailAPI(generics.RetrieveAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user)
