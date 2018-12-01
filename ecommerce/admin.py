from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ecommerce.models import Marca, Produto, Filial, Cliente, Endereco, Pedido, PedidoItem, Parcela


@admin.register(Filial)
class FilialResource(ImportExportModelAdmin):
    pass


@admin.register(Marca)
class MarcaResource(ImportExportModelAdmin):
    pass


@admin.register(Produto)
class ProdutoResource(ImportExportModelAdmin):
    pass


@admin.register(Cliente)
class ClienteResource(ImportExportModelAdmin):
    pass


@admin.register(Endereco)
class EnderecoResource(ImportExportModelAdmin):
    pass


@admin.register(Pedido)
class PedidoResource(ImportExportModelAdmin):
    pass


@admin.register(PedidoItem)
class PedidoItemResource(ImportExportModelAdmin):
    pass


@admin.register(Parcela)
class ParcelaItemResource(ImportExportModelAdmin):
    pass
