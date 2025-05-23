from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from products.models.product import Product
from products.serializers.product_serializer import ProductSerializer

from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_products(request):
    ''' Listar productos '''
    list_products = Product.objects.all() # select * from productos
    serializer = ProductSerializer(list_products, many = True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):
    ''' Crear producto '''
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detail_product(request, product_id):
    product = get_object_or_404(Product, id = product_id) # Busca

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
    

    
    if request.method == 'DELETE':
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_product(request, product_id):
    product = get_object_or_404(Product, id = product_id) # Busca
    ''' otra logíca '''
    serializer = ProductSerializer(product, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
    
@api_view(['GET'])
def show_product(request, product_id):
    product = get_object_or_404(Product, id = product_id) # Busca
    serializer = ProductSerializer(product)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_product(request, product_id):
    product = get_object_or_404(Product, id = product_id) # Busca
    product.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)

