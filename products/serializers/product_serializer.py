from decimal import Decimal
from rest_framework import serializers
from products.models.product import Product
from products.models.category import Category
from .category_serializer import CategorySerializer


def validate_unique_name(value):
    if Product.objects.filter(name__iexact = value).exists():
        raise serializers.ValidationError("Ya existe un producto con ese nombre.")
    else:
        return value


class ProductSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=100, validators=[validate_unique_name])
    
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        allow_null = True,
        required = True,
        source = 'category'
    )
    

    offer_price = serializers.SerializerMethodField()
    def get_offer_price(self, instace):
        discount = Decimal('0.85')
        return instace.price * discount

    class Meta:
        model = Product
        #fields = ['id','name', 'description', 'price', 'offer_price'] == fields = '__all__'
        fields = '__all__'
