from django.urls import path, include
from products.views.product_view import list_products, create_product, detail_product

### Importar viewset
from rest_framework.routers import DefaultRouter
from products.views.category_view import CategoryViewSet
from products.views.tag_view import TagViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tags', TagViewSet, basename='tag')
#router_tag = DefaultRouter()
#router_tag.register(r'tags', TagViewSet, basename='tag')


urlpatterns = [
    path('', include(router.urls)),

    path('products/', list_products, name='lista_de_productos'),
    path('products/create/', create_product, name='crear_producto'),
    path('products/<int:product_id>', detail_product, name='detalles_del_producto' )
]
'''
GET /categories/ -> listar todas las categorias
POST /categories/ -> Crear mnueva categoria
GET /categories/{id} -> ver una sola categoria
PUT /categories/{id} -> actualizar una categoria
DELETE /categories/{id} -> eliminar una categoria
'''