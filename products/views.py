from rest_framework import status
from rest_framework.response import Response
from .models import Product, Category, Review
from rest_framework import viewsets
from .serializers import ProductSerializer, ProductValidateSerializer, CategorySerializer, ReviewSerializer, \
    ReviewValidateSerializer, CategoryValidateSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = request.validated_data.get('title')
        description = request.validated_data.get('description')
        price = request.validated_data.get('price')
        category = request.validated_data.get('category')

        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            category=category
        )
        product.save()
        return Response(status=status.HTTP_201_CREATED, data=ProductSerializer(product).data)

    def update(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response(data={'error_message': 'Product not found'})

        if request.method == 'PUT':
            serializer = ProductValidateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            product.title = request.validated_data.get('title')
            product.descriptions = request.validated_data.get("descriptions")
            product.price = request.validated_data.get("price")
            product.category_id = request.validated_data.get("category")
            product.save()

            return Response(data=ProductSerializer(product).data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = request.validated_data.get('name')
        category = Product.objects.create(
            name=name
        )
        category.save()
        return Response(status=status.HTTP_201_CREATED, data=CategorySerializer(category).data)

    def update(self, request, *args, **kwargs):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response(data={'error_message': 'Category not found'})

        if request.method == 'PUT':
            serializer = CategoryValidateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            category.name = request.validated_data.get('name')
            category.save()

            return Response(data=ProductSerializer(category).data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = request.validated_data.get('text')
        product = request.validated_data.get('product')
        stars = request.validated_data.get('stars')
        review = Product.objects.create(
            text=text,
            product=product,
            stars=stars
        )
        review.save()
        return Response(status=status.HTTP_201_CREATED, data=ReviewSerializer(review).data)

    def update(self, request, *args, **kwargs):
        try:
            review = Review.objects.get(id=id)
        except Review.DoesNotExist:
            return Response(data={'error_message': 'Review not found'})

        if request.method == 'PUT':
            serializer = ReviewValidateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            review.text = request.validated_data.get('text')
            review.product = request.validated_data.get('product')
            review.stars = request.validated_data.get('stars')
            review.save()

            return Response(data=ProductSerializer(review).data)