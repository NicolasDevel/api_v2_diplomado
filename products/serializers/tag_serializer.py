from rest_framework import serializers
from products.models.tag import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        extra_kwargs = {
            'name' : { 'required': True, 'allow_blank': False }
        }
