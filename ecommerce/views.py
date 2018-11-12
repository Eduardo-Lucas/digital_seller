from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import permissions

from ecommerce.models import Marca, Produto
from ecommerce.serializers import MarcaSerializer, ProdutoSerializer


class MarcaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Permitir consultar dados cadastrais de marcas.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Marca.objects.all().order_by('nm_marca')
    serializer_class = MarcaSerializer
    filter_fields = ('cd_marca',)


class ProdutoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Permitir consultar dados cadastrais de produtos. Variações de produtos devem ser retornadas em
    objeto ou vetor dentro de posições. Retorno deve ser ordenado pelo código do produto em ordem
    ascendente.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Produto.objects.all().order_by('cd_produto')
    serializer_class = ProdutoSerializer
    filter_fields = ('cd_produto',)


# Consultar fila de produtos cadastrados (/api/produtos/consultar/fila/inseridos)
class ProdutoInseridoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Permitir consultar produtos cadastrados no ERP a partir de uma determinada data e hora.
    Variações de produtos devem vir em objeto ou vetor dentro de posições. Retorno deve ser
    ordenado pela data e hora do cadastro do produto em ordem ascendente.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Produto.objects.all().order_by('dt_cadastro', 'hr_cadastro')
    serializer_class = ProdutoSerializer
    filter_fields = ('dt_cadastro', 'hr_cadastro')
