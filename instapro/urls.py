
from django.http import HttpResponseRedirect
from django.contrib import admin
from user import views
from django.urls import path
from user.views import registryView, LoginView, SpamView, SearchView, user_detail

urlpatterns = [
    path('',views.home, name='Home'),
    path('admin/', admin.site.urls),
    path('api/register/', registryView, name='register'),
    path('api/login/', LoginView, name='login'),
    path('api/spam/', SpamView, name='spams'),
    path('api/search/?q=', SearchView, name='search'),
    path('api/user-detail/<str:phone_number>/', user_detail, name='user-detail'),
]
