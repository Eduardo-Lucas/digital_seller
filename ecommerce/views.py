from rest_framework import viewsets
from rest_framework import permissions

from ecommerce.models import Marca, Produto
from ecommerce.serializers import MarcaSerializer, ProdutoSerializer


class MarcaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint da API que permite que as Marcas sejam visualizadas.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Marca.objects.all().order_by('nm_marca')
    serializer_class = MarcaSerializer


class ProdutoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint da API que permite que as Produtos sejam visualizados.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Produto.objects.all().order_by('nm_produto')
    serializer_class = ProdutoSerializer
