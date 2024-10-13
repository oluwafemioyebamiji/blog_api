from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Category, Article
from articles import serializers

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CategoryEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticlewithCategorySerializer


class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer

class ArticleEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class ArticleEditWithSlugView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    lookup_field = 'slug'




class CategorywithArticlesListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorywithArticlesSerializer
