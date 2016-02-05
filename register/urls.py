from django.conf.urls import include,url,patterns
from django.views.generic import TemplateView
from register.views import *
from register.models import *
from register import *

from django.contrib.auth.decorators import login_required

urlpatterns = [
        url(r'^signup/$', UserRegistrationView.as_view(), name='signup'),
        url(r'^success/', TemplateView.as_view(template_name='success.html'),name='success'),
        url(r'^user/profile/$', UserProfileView.as_view(), name='user_profile'),
        url(r'^$', TemplateView.as_view(template_name='logout.html'),name='logout'),
        ]