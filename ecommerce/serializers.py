from rest_framework import serializers

from ecommerce.models import Marca, Produto, Cliente


class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('url', 'cd_marca', 'nm_marca')


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    nm_marca = serializers.ReadOnlyField(source='marca.nm_marca')
    
    class Meta:
        model = Produto
        fields = ('url', 'cd_produto', 'nm_produto', 'dc_modelo', 'cd_barras', 'cd_altura', 'nr_comprimento',
                  'nr_largura', 'nr_peso', 'dt_cadastro', 'hr_cadastro', 'dt_alteracao', 'hr_alteracao',
                  'dt_preco', 'hr_preco', 'fl_situacao', 'nm_marca', 'qt_estoque', 'vl_preco')


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('url', 'cd_cliente_eco', 'cd_cliente_erp', 'nr_cpf', 'nr_cnpj', 'nm_cliente', 'dt_nascimento',
                  'tp_pessoa', 'fl_contribuinte_icms', 'nr_rg', 'dc_orgao', 'dt_cadastro', 'nr_fone_residencia',
                  'nr_fone_celular', 'nm_razao_social', 'nr_inscricao_estadual')
