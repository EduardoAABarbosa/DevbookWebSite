from rest_framework import serializers
from core import models

class DepoimentoSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Depoimentos
        fields='__all__'