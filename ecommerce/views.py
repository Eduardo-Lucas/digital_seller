from rest_framework import viewsets
from rest_framework import permissions
from ecommerce.models import Marca
from ecommerce.serializers import MarcaSerializer


class MarcaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Marca.objects.all().order_by('nm_marca')
    serializer_class = MarcaSerializer
