from import_export import resources

from ecommerce.models import Marca, Produto


class MarcaResource(resources.ModelResource):
    class Meta:
        model = Marca
        fields = ('id', 'cd_marca', 'nm_marca',)


class ProdutoResource(resources.ModelResource):
    class Meta:
        model = Produto
        fields = ('id', 'cd_produto', 'nm_produto', 'dc_modelo', 'cd_barras', 'cd_altura', 'nr_comprimento',
                  'nr_largura', 'nr_peso', 'dt_cadastro', 'fl_situacao', 'nm_marca')
