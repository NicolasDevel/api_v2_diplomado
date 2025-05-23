from rest_framework import viewsets
from products.models.tag import Tag
from products.serializers.tag_serializer import TagSerializer

from rest_framework.permissions import IsAuthenticated

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('-id')
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
