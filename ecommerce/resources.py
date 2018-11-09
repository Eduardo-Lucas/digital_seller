from import_export import resources

from ecommerce.models import Marca


class MarcaResource(resources.ModelResource):
    class Meta:
        model = Marca
        fields = ('id', 'cd_marca', 'nm_marca',)
