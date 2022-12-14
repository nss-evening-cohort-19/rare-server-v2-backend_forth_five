from rarev2api.models import Category
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status


class CategoryView(ViewSet):
    
    def list(self, request):
        
        categories = Category.objects.all()
        
        serializer = CategorySerializer(categories, many=True)
        
        cat_format = serializer.data
        for cat in cat_format:
            cat['value'] = cat.pop('id')
        return Response(cat_format)
    
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoryfields = ('id', 'label')
        