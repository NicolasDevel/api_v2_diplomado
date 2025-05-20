from django.urls import path
from products.views.product_view import list_products, create_product, detail_product

urlpatterns = [
    path('products/', list_products, name='lista_de_productos'),
    path('products/create/', create_product, name='crear_producto'),
    path('products/<int:product_id>', detail_product, name='detalles_del_producto' )
]
