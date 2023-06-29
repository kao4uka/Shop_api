from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, Review, Category


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product stars'.split()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name product_count'.split()


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    filtered_review_list = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = 'id title descriptions price category filtered_review_list avg_rating'.split()


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=100)
    description = serializers.CharField()
    price = serializers.IntegerField()
    category = serializers.IntegerField()


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=3)
    product = serializers.IntegerField()
    stars = serializers.IntegerField(default=5)


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=50)

