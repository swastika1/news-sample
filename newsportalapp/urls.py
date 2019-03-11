
from django.urls import path
from .views import *

app_name = 'newsportalapp'

urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('news/list/', NewsListView.as_view(), name="newslist"),
    path('news/<int:pk>/detail/', NewsDetailView.as_view(), name="newsdetail"),
    path('search/result/', SearchResultView.as_view(), name="searchresult"),
    path('news/create/', NewsCreateView.as_view(), name="newscreate"),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name="newsupdate"),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name="newsdelete"),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name="categorydetail"),
    path('login/', LoginView.as_view(), name="adminlogin"),
    path('logout/', LogoutView.as_view(), name="adminlogout"),
    path('register/', RegisterView.as_view(), name="register"),





]
