from django.views.generic import *
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allcategory'] = Newscategory.objects.all()
        return context


class HomeView(BaseMixin, TemplateView):
    template_name = 'home.html'


class NewsListView(BaseMixin, ListView):
    template_name = 'newslist.html'
    model = News
    context_object_name = 'newslist'


class NewsDetailView( BaseMixin, DetailView):
    login_url = '/login'
    template_name = 'newsdetail.html'
    model = News
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newslist'] = News.objects.all()
        return context


class SearchResultView(BaseMixin, TemplateView):
    template_name = 'searchresult.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            lookup = Q(title__icontains=query)
            slist = News.objects.filter(lookup)
            context["slist"] = slist
        return context


class NewsCreateView( BaseMixin, CreateView):
    login_url = '/login'
    template_name = 'newscreate.html'
    form_class = NewsForm
    success_url = "/news/list"


class NewsUpdateView(BaseMixin, UpdateView):
    template_name = 'newscreate.html'
    form_class = NewsForm
    model = News
    success_url = '/news/list'


class NewsDeleteView(BaseMixin, DeleteView):
    template_name = 'newsdelete.html'
    model = News
    form_class = NewsForm
    success_url = '/news/list'


class CategoryDetailView(BaseMixin, DetailView):
    template_name = 'categorydetail.html'
    model = Newscategory
    context_object_name = "categorydetail"


class LoginView(BaseMixin, FormView):
    template_name = "logins.html"
    form_class = LoginForm
    success_url = '/news/create'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        else:
            return render(self.request,
                          self.template_name,
                          {'form': form, 'errors': 'user info not found'})
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterView(BaseMixin, CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'
