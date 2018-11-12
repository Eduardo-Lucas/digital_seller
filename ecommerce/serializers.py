from rest_framework import serializers

from ecommerce.models import Marca, Produto


class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('url', 'cd_marca', 'nm_marca')


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    nm_marca = serializers.ReadOnlyField(source='marca.nm_marca')
    
    class Meta:
        model = Produto
        fields = ('url', 'cd_produto', 'nm_produto', 'dc_modelo', 'cd_barras', 'cd_altura', 'nr_comprimento',
                  'nr_largura', 'nr_peso', 'dt_cadastro', 'hr_cadastro', 'fl_situacao', 'nm_marca')
