from rest_framework import viewsets
from rest_framework import permissions

from ecommerce.models import Marca, Produto, Cliente, Endereco
from ecommerce.serializers import MarcaSerializer, ProdutoSerializer, ClienteSerializer, EnderecoSerializer


class MarcaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Permitir consultar dados cadastrais de marcas.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Marca.objects.all().order_by('nm_marca')
    serializer_class = MarcaSerializer
    filter_fields = ('cd_marca', )


# Consultar produtos (/api/produtos/consultar)
class ProdutoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Permitir consultar dados cadastrais de produtos. Variações de produtos devem ser retornadas em
    objeto ou vetor dentro de posições. Retorno deve ser ordenado pelo código do produto em ordem
    ascendente.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Produto.objects.all().order_by('cd_produto')
    serializer_class = ProdutoSerializer
    filter_fields = ('cd_produto', 'dt_cadastro', 'hr_cadastro', 'dt_alteracao', 'hr_alteracao')


# Consultar clientes (/api/clientes/consultar)
class ClienteViewSet(viewsets.ModelViewSet):
    """
    Permitir inserir, consultar e alterar dados cadastrais de Cliente.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Cliente.objects.all().order_by('cd_cliente_erp')
    serializer_class = ClienteSerializer
    filter_fields = ('cd_cliente_eco', 'cd_cliente_erp', 'nr_cpf', 'nr_cnpj')


# Consultar endereços (/api/endereços/consultar)
class EnderecoViewSet(viewsets.ModelViewSet):
    """
    Permitir inserir, consultar e alterar dados cadastrais de Endereços de Cliente.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Endereco.objects.all().order_by('cd_endereco_erp')
    serializer_class = EnderecoSerializer
    filter_fields = ('cliente', 'cd_endereco_erp', )
