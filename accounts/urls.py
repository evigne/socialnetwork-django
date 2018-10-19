from django.conf.urls import url
from django.contrib.auth.views import (LoginView,LogoutView,
                                       PasswordResetView,PasswordResetDoneView,
                                       PasswordResetConfirmView,PasswordResetCompleteView)
from . import views

app_name = 'accounts'  #for name space

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^login/$',LoginView.as_view(template_name= 'accounts/login.html'),name='login'),
    url(r'^logout/$',LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'^profile/$',views.view_profile, name='view_profile'),
    url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),
    url(r'^change-password/$',views.change_password,name='change_password'),
    url(r'^reset-password/$',PasswordResetView.as_view(template_name='accounts/reset_password.html'),name='reset_password'),


    url(r'^reset-password/done/$',PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'),name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-zA-z]+)-(?P<token>.+)/$',PasswordResetConfirmView.as_view(template_name='accounts/reset_password_confirm.html'),name='password_reset_confirm'),
    url(r'^reset-password/complete/$',PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'),name='password_reset_complete'),

]

"""

Error: [Errno 111] Connection refused

To run locally for Debugging Purpose

Ref_link: https://stackoverflow.com/questions/5802189/django-errno-111-connection-refused/5802348#5802348

"""