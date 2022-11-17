from rest_framework import serializers
from .models import KoalaDB

class KoalaDBSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = KoalaDB
        fields = [
            'koala_id',
            'sex',
            'dob',
            'gender'
        ]
