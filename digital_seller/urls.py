from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from ecommerce.views import MarcaViewSet, ProdutoViewSet, ClienteViewSet, EnderecoViewSet, PedidoViewSet, FilialViewSet


router = routers.DefaultRouter()
router.register('api/filiais', FilialViewSet,)
router.register('api/marcas', MarcaViewSet,)
router.register('api/produtos', ProdutoViewSet,)
router.register('api/clientes', ClienteViewSet,)
router.register('api/enderecos', EnderecoViewSet,)
router.register('api/pedidos', PedidoViewSet,)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    
]
