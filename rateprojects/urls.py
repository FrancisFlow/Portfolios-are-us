from django.urls import path
from . import views


urlpatterns= [
    path('', views.home, name='home'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('new_project/', views.new_post, name='new_project'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('single_project/<project_name>/', views.single_project, name='single_project'),
    path('search/', views.search_results, name='search_results'),
    path('review/<id>/', views.review, name='review'),
]