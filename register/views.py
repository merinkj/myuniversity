from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from register.models import *
from register.forms import *

from django.views.generic.detail import DetailView


# Create your views here.
class Home(TemplateView):
    template_name = "index.html"

class CourseView(TemplateView):
    template_name = "courselist.html"

class SignView(TemplateView):
    template_name = "login.html"

class UserRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "signup.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = '/register/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)


class UserLoginView(AnonymousRequiredMixin, FormView):
    template_name = "signin.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = '/register/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)

class CurrentUserMixin(object):
    model = User

    def get_object(self, *args, **kwargs):
        try: obj = super(CurrentUserMixin, self).get_object(*args, **kwargs)
        except AttributeError: obj = self.request.user
        return obj

class UserProfileView(LoginRequiredMixin, CurrentUserMixin, DetailView):
    pass
