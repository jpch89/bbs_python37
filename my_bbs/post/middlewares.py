from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class FirstMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('FirstMiddleware: process_request')
        # return JsonResponse({'Hello': 'Django BBS'})
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('FirstMiddleware: process_view')
        # return JsonResponse({'Hello': 'Django BBS'})
    
    def process_response(self, request, response):
        print('FirstMiddleware: process_response')
        return response
    
    def process_exception(self, request, exception):
        print('FirstMiddleware: process_exception')
        return JsonResponse({'exception': str(exception)})
    
    def process_template_response(self, request, response):
        print('FirstMiddleware: process_template_response')
        return response


class SecondMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('SecondMiddleware: process_request')
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('SecondMiddleware: process_view')
    
    def process_response(self, request, response):
        print('SecondMiddleware: process_response')
        return response
