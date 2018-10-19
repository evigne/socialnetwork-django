
import re

from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout



EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings,'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response



    def process_view(self,request,view_func,view_args,view_kwargs):
        """
        https://docs.djangoproject.com/en/2.1/topics/http/middleware/#process-view
        process_view()¶
        process_view(request, view_func, view_args, view_kwargs)¶
        request is an HttpRequest object. view_func is the Python function that Django is about to use. (It’s the actual
        function object, not the name of the function as a string.) view_args is a list of positional arguments that will
        be passed to the view, and view_kwargs is a dictionary of keyword arguments that will be passed to the view. Neither
         view_args nor view_kwargs include the first view argument (request).

        process_view() is called just before Django calls the view.

        It should return either None or an HttpResponse object. If it returns None, Django will continue processing
        this request, executing any other process_view() middleware and, then, the appropriate view. If it returns an HttpResponse
        object, Django won’t bother calling the appropriate view; it’ll apply response middleware to that HttpResponse and return
        the result.

       """
        assert hasattr(request,'user')
        path = request.path_info.lstrip('/')
        print(path)
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if path == 'account/logout/':
            logout(request)
        

         # if not request.user.is_authenticated:
        #     if not any(url.match(path) for url in EXEMPT_URLS):
        #         return redirect(settings.LOGIN_URL)
        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)

