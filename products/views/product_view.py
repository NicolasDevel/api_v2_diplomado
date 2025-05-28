from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from products.models.product import Product
from products.serializers.product_serializer import ProductSerializer

from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail

#Para crear archivos
from django.http import HttpResponse, JsonResponse
from openpyxl import Workbook
from io import BytesIO
from datetime import datetime



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
    serializer = ProductSerializer(
        data = request.data, 
        context = {'request' : request}
        )
    if serializer.is_valid():
        serializer.save()

        subject = 'Producto creado'
        message = 'Has creado un producto mediante la aplicación'
        recipient_list = [request.user.email]

        send_mail(
            subject,
            message,
            None,
            recipient_list,
            fail_silently=True #Va lanzar una excepcion (raise) si el envio falla
        )

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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def show_product(request, product_id):
    product = get_object_or_404(Product, id = product_id) # Busca
    serializer = ProductSerializer(product)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, product_id):
    product = get_object_or_404(Product, id = product_id) # Busca
    product.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def export_products_to_excel(request):
    #Crear el libro
    instance_workbook = Workbook()
    work_sheet = instance_workbook.active
    work_sheet.title = 'Productos'

    headers = [
        'ID',
        'Nombre',
        'Descripción',
        'Precio',
        'Categoría',
        'Tags',
        'Usuario',
    ]
    work_sheet.append(headers)

    products = Product.objects.select_related('category', 'user').prefetch_related('tags').all()

    for product in products:
        tags = ', '.join([tag.name for tag in product.tags.all()])

        work_sheet.append([
            product.id,
            product.name,
            product.description,
            float(product.price),
            product.category.name,
            tags,
            product.user.first_name if product.user else ""
        ])
    #Crear respuesta
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    date = datetime.now().strftime('%Y-%m-%d')
    name_file = f"productos_{date}.xlsx"
    
    response['Content-Disposition'] = f'attachment; filename={name_file}'

    #Guardar y enviar
    buffer = BytesIO()
    instance_workbook.save(buffer)

    response.write(buffer.getvalue())

    return response

    
