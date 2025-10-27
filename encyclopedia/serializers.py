from rest_framework import serializers
from .models import Category, Entry


class CategorySerializer(serializers.ModelSerializer):
    """分类序列化器"""
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']


class EntrySerializer(serializers.ModelSerializer):
    """词条序列化器"""
    categories = CategorySerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Entry
        fields = [
            'id', 'title', 'summary', 'content', 
            'categories', 'created_by', 'created_at', 'updated_at'
        ]


class EntryCreateSerializer(serializers.ModelSerializer):
    """词条创建序列化器"""
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        many=True, 
        required=False
    )
    
    class Meta:
        model = Entry
        fields = ['title', 'summary', 'content', 'categories']
    
    def create(self, validated_data):
        categories = validated_data.pop('categories', [])
        entry = Entry.objects.create(**validated_data)
        entry.categories.set(categories)
        return entry
    
    def update(self, instance, validated_data):
        categories = validated_data.pop('categories', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if categories is not None:
            instance.categories.set(categories)
        
        return instance