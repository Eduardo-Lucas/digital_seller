from import_export import resources

from ecommerce.models import Marca, Produto, Filial, Cliente


class FilialResource(resources.ModelResource):
    class Meta:
        model = Filial
        fields = ('id', 'nome', )


class MarcaResource(resources.ModelResource):
    class Meta:
        model = Marca
        fields = ('id', 'cd_marca', 'nm_marca',)


class ProdutoResource(resources.ModelResource):
    class Meta:
        model = Produto
        fields = ('id', 'cd_produto', 'nm_produto', 'dc_modelo', 'cd_barras', 'cd_altura', 'nr_comprimento',
                  'nr_largura', 'nr_peso', 'dt_cadastro', 'fl_situacao', 'nm_marca', 'qt_estoque', 'vl_preco')


class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente
        fields = ('id', 'cd_cliente_eco', 'cd_cliente_erp', 'nr_cpf', 'nr_cnpj', 'nm_cliente', 'dt_nascimento',
                  'tp_pessoa', 'fl_contribuinte_icms', 'nr_rg', 'dc_orgao', 'dt_cadastro', 'nr_fone_residencia',
                  'nr_fone_celular', 'nm_razao_social', 'nr_inscricao_estadual')