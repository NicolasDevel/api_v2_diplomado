from rest_framework import serializers
from products.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description'] # '__all__'
        extra_kwargs = {
            'name' : { 'required': True, 'allow_blank': False }
        }