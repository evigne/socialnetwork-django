from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns=[
    url(r'^$',views.home),
    url(r'login/$',LoginView.as_view(template_name= 'accounts/login.html')),
    url(r'logout/$',LogoutView.as_view(template_name='accounts/logout.html')),
]
