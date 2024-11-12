# jobs/urls.py
from django.contrib import admin
from django.urls import path
from jobs import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('', views.user_login, name='login'),
    path('search/', views.search_jobs, name='search_jobs'),
    path('logout/', views.logout_view, name='logout'), 
]
