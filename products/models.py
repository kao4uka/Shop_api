from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def product_count(self):
        return self.objects.all()


class Product(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def filtered_review_list(self):
        return self.review_list.filter(stars__gt=3)

    @property
    def avg_rating(self):
        lis = [review.stars for review in self.filtered_review_list.all()]
        return sum(lis) / len(lis)


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review_list')
    stars = models.IntegerField(default=5, choices=((i, '* ' * i) for i in range(1, 6)))
