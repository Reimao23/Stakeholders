from django.urls import path
from stakeholders import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.sign_up, name='sign_up'),
    path("", views.home, name="home"),
    path('profile/', views.profile_view, name='profile'),
    path('inscricao', views.inscricao_view, name='inscricao'),
    path('logininscricao/', views.logininscricao_view, name='logininscricao'),
    path('inscricaoregisto', views.inscricaoregisto_view, name='inscricaoregisto'),
]