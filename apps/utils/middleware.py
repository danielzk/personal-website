from django.utils.deprecation import MiddlewareMixin
from django.utils import translation

# TODO: remove this when new languages are added

class LangMiddleware(MiddlewareMixin):
    def process_request(self, request):
        translation.activate('es')
        request.LANGUAGE_CODE = translation.get_language()
