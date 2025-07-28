import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"[{datetime.now()}] {request.method} {request.path} by {request.user if request.user.is_authenticated else 'Anonymous'}")
        response = self.get_response(request)
        return response
