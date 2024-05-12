from rest_framework import serializers
from .models import Paragraph


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['unique_id', 'text']
