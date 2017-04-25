"""mardjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.auth.views import login,logout
from django.contrib import admin
# from polls.admin import admin_site
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.views.static import serve
from .settings import local

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="introduce.html"), name='index'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^dashboard/', TemplateView.as_view(template_name="dashboad.html"), name='index'),

    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': local.MEDIA_ROOT,
    }),
    url(r'^static/(?P<path>.*)$', serve, {
        'document_root': local.STATIC_ROOT,
    }),
]