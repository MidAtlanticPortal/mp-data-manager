from rest_framework import serializers
from .models import Layer, LookupInfo


class BriefLayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = ('id', 'name', 'layer_type', 'url', 'opacity', 'vector_color', 'vector_fill', 'vector_outline_color', 'vector_outline_opacity', 'lookup_field', 'lookup_table', 'arcgis_layers')

class LookupInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LookupInfo
