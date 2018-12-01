from rest_framework import serializers
from rest_framework.versioning import URLPathVersioning

from ecommerce.models import Marca, Produto, Cliente, Endereco, Pedido, Filial, PedidoItem


class VersionSerializer(URLPathVersioning):
    default_version = 'v1'


class FilialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Filial
        fields = ('url', 'nome',)


class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('url', 'cd_marca', 'nm_marca')


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    nm_marca = serializers.ReadOnlyField(source='marca.nm_marca')

    class Meta:
        model = Produto
        fields = ('url', 'filial', 'cd_produto', 'nm_produto', 'dc_modelo', 'cd_barras', 'cd_altura', 'nr_comprimento',
                  'nr_largura', 'nr_peso', 'dt_cadastro', 'hr_cadastro', 'dt_alteracao', 'hr_alteracao',
                  'dt_preco', 'hr_preco', 'fl_situacao', 'nm_marca', 'qt_estoque', 'vl_preco')


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('url', 'cd_cliente_eco', 'cd_cliente_erp', 'nr_cpf', 'nr_cnpj', 'nm_cliente', 'dt_nascimento',
                  'tp_pessoa', 'fl_contribuinte_icms', 'nr_rg', 'dc_orgao', 'dt_cadastro', 'nr_fone_residencia',
                  'nr_fone_celular', 'nm_razao_social', 'nr_inscricao_estadual')


class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = ('url', 'cliente', 'cd_endereco_erp', 'nr_cep', 'dc_endereco', 'dc_numero', 'dc_complemento',
                  'dc_bairro', 'nm_cidade', 'sg_uf')


class PedidoItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PedidoItem
        fields = ('url', 'produto', 'vl_venda')


class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.StringRelatedField(many=True)
    parcelas = serializers.StringRelatedField(many=True)

    class Meta:
        model = Pedido
        fields = ('url', 'filial', 'cliente', 'nr_pedido_eco', 'nr_pedido_erp', 'dt_pedido',
                  'hr_pedido', 'cd_vendedor', 'dc_observacao', 'tp_entrega', 'vl_entrega', 'items', 'parcelas')
