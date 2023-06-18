from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, Review
from serializers import ProductSerializer, ProductReviewSerializer, CategorySerializer, ReviewSerializer


@api_view(["GET"])
def product_review_list(request):
    products_reviews = Product.objects.all()
    serializer = ProductReviewSerializer(products_reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        data = ProductSerializer(product, many=True).data

        return Response(data=data)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category = request.data.get('category')

        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            category=category
        )
        product.save()
        return Response(status=status.HTTP_201_CREATED, data=ProductSerializer(product).data)



@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': "Product not found!"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = ProductSerializer(product).data
        return Response(data=data)
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        product.title = request.data.get('title')
        product.descriptions = request.data.get("descriptions")
        product.price = request.data.get("price")
        product.category_id = request.data.get("category")
        product.save()
        return Response(data=ProductSerializer(product).data)


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        data = CategorySerializer(category, many=True).data

        return Response(data=data)

    elif request.method == 'POST':
        name = request.data.get('name')
        category = Product.objects.create(
            name=name
        )
        category.save()
        return Response(status=status.HTTP_201_CREATED, data=CategorySerializer(category).data)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': "Category not found!"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = CategorySerializer(category).data
        return Response(data=data)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        category.name = request.data.get('name')
        return Response(data=CategorySerializer(category).data)


@api_view(["GET", "POST"])
def review_list_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(review, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        text = request.data.get('text')
        product = request.data.get('product')
        stars = request.data.get('stars')
        review = Product.objects.create(
            text=text,
            product=product,
            stars=stars
        )
        review.save()
        return Response(status=status.HTTP_201_CREATED, data=ReviewSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': "Review not found!"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        review.text = request.data.get('text')
        review.product = request.data.get('product')
        review.stars = request.data.get('stars')
        return Response(data=CategorySerializer(review).data)

