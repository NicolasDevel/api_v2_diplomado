from decimal import Decimal
from rest_framework import serializers
from products.models.product import Product
from products.models.category import Category
from products.models.tag import Tag
from .category_serializer import CategorySerializer
from .tag_serializer import TagSerializer


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

    #datos de la relacion con tag
    tags_id = serializers.PrimaryKeyRelatedField(
        queryset = Tag.objects.all(),
        many = True,
        allow_null = True,
        required = False,
        write_only = True,
        source = 'tags' # Asegurensen de que coincida con el nombre que tiene el campo en el modelo
    )

    category = CategorySerializer(
        read_only=True
    )
    
    tags = TagSerializer(
        many = True,
        read_only = True
    )

    #Agregar usuario
    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )

    offer_price = serializers.SerializerMethodField()
    def get_offer_price(self, instace):
        discount = Decimal('0.85')
        return instace.price * discount
    
    ''' Eventos '''
    
    def create(self, validated_data):
        ''' 
        Sobrescribir el evento crear del 
        serializador para poder manejar la relacion muchos a muchos 
        '''
        tags_data = validated_data.pop('tags', [])

        product = Product.objects.create(**validated_data)

        #Añadir los tags al producto
        if tags_data:
            product.tags.set(tags_data)

        return product
    
    def update(self, instance, validated_data):
        ''' 
        Sobrescribir el evento actualizar del 
        serializador para poder manejar la relacion muchos a muchos 
        '''
        tags_data = validated_data.pop('tags', None)
        
        #Actualizo los campos normales
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        #Actualizar los tags si se han enviado en el json
        if tags_data is not None:
            instance.tags.set(tags_data)


    class Meta:
        model = Product
        #fields = ['id','name', 'description', 'price', 'offer_price'] == fields = '__all__'
        fields = '__all__'

        
