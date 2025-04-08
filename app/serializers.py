from rest_framework import serializers
from .models import Movie

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title','name','price','description']