from ecommerce.models import Marca
from rest_framework import serializers


class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('cd_marca', 'nm_marca')
