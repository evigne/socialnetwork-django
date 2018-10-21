"""sitenew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login_redirect ,name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/',include('accounts.urls',namespace='accounts')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
Serving files uploaded by a user during development¶
During development, you can serve user-uploaded media files from MEDIA_ROOT using the django.views.static.serve() view.

This is not suitable for production use! For some common deployment strategies, see Deploying static files.

For example, if your MEDIA_URL is defined as /media/, you can do this by adding the following snippet to your urls.py:

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""