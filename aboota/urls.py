from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.apps import apps
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf.urls import url
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from debug_toolbar import urls as durls
from django.conf.urls import re_path
from home import views

# handler404 = 'home.views.error_404'
# handler500 = 'home.views.error_500'
# handler403 = 'home.views.error_403'
# handler400 = 'home.views.error_400'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    path('', TemplateView.as_view(template_name='base.html')),
    path('about', TemplateView.as_view(template_name='about.html')),
    path('accounts', TemplateView.as_view(template_name='accounts.html')),
    path('awards', TemplateView.as_view(template_name='awards.html')),
    path('contact', TemplateView.as_view(template_name='contact.html')),
    path('contest', TemplateView.as_view(template_name='contest.html')),
    path('cookie', TemplateView.as_view(template_name='cookie.html')),
    path('disclaimer', TemplateView.as_view(template_name='disclaimer.html')),
    path('education', TemplateView.as_view(template_name='education.html')),
    path('faq', TemplateView.as_view(template_name='faq.html')),
    path('feature', TemplateView.as_view(template_name='feature.html')),
    path('partnership', TemplateView.as_view(template_name='partnership.html')),
    path('platform', TemplateView.as_view(template_name='platform.html')),
    path('privacy', TemplateView.as_view(template_name='privacy.html')),
    path('products', TemplateView.as_view(template_name='products.html')),
    path('promotions', TemplateView.as_view(template_name='promotions.html')),
    path('terms', TemplateView.as_view(template_name='terms.html')),
    path('trading-hours', TemplateView.as_view(template_name='trading-hours.html')),
    path('open-live', views.live),
    path('open-demo', views.demo),
    path('contact-us', views.contact),
    path('account/', include("allauth.urls")),
    path('__debug__/', include(durls), name='debug_toolbar'),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path("api-auth/", include("rest_framework.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]