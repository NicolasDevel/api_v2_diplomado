from rest_framework import viewsets
from products.models.category import Category
from products.serializers.category_serializer import CategorySerializer

from rest_framework.permissions import IsAuthenticated

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
