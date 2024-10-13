from rest_framework import serializers
from .models import Article, Category


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ("id","title","is_published","body","category")
        read_only_fields = ('id',)



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("id","title","is_published")
        read_only_fields = ('id',)


class ArticlewithCategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = ("id","title","slug","is_published","body","category")
        read_only_fields = ('id',)

class ArticleContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ("id","title","body")
        read_only_fields = ('id',)

class CategorywithArticlesSerializer(serializers.ModelSerializer):
    relatedarticles = serializers.SerializerMethodField()
    somerandomnonsense = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id","title","is_published", "relatedarticles", "somerandomnonsense")
        read_only_fields = ('id',)

    def get_relatedarticles(self, obj):
        articlelist = Article.objects.filter(is_published=True, category = obj.id)
        return ArticleContentSerializer(articlelist, many=True).data
    
    def get_somerandomnonsense(self, obj):
        return f"This is some random nonsense for id {obj.id}"