from django.contrib import admin
from django.urls import path, include
from products.views import ProductViewSet, CategoryViewSet, ReviewViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('prouduct', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('review', ReviewViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
