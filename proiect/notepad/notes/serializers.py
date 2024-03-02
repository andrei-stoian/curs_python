from rest_framework import serializers
from .models import Notes

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'title', 'text', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']