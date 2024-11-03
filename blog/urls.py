"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from articles import views
from users.views import CustomRegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("category/list/", views.CategoryListView.as_view()),
    path("category/create/", views.CategoryCreateView.as_view()),
    path("category/edit/<pk>/", views.CategoryEditView.as_view()),
    path("article/list/", views.ArticleListView.as_view()),
    path("article/create/", views.ArticleCreateView.as_view()),
    path("article/edit/<pk>/", views.ArticleEditView.as_view()),
    path("article/slug/<slug>/", views.ArticleEditWithSlugView.as_view()),
    path("categoryarticles/list/", views.CategorywithArticlesListView.as_view()),
         
    path("auth", include('django.contrib.auth.urls')),
    path("api/auth/", include('dj_rest_auth.urls')),
    path("api/auth/registration/", include('dj_rest_auth.registration.urls')),
    path("auth/signup/", CustomRegisterView.as_view()),
    


]
