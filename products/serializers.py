from rest_framework import serializers
from .models import Product, Review, Category


class ReviewSerializer(serializers.Serializer):
    class Meta:
        model = Review
        fields = 'id text product stars'.split()


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = 'id name product_count'.split()


class ProductReviewSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = 'id title description price category avg_rating'.split()