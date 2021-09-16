from rest_framework import viewsets
from core.api import serializers
from core import models

class DepoimentosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.DepoimentoSerializers
    queryset = models.Depoimentos.objects.all()