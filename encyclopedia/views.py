from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Category, Entry
from .serializers import CategorySerializer, EntrySerializer, EntryCreateSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class EntryViewSet(viewsets.ModelViewSet):
    """词条视图集"""
    queryset = Entry.objects.select_related('created_by').prefetch_related('categories').all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return EntryCreateSerializer
        return EntrySerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        """搜索词条"""
        query = request.query_params.get('q', '')
        if query:
            entries = self.queryset.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query) |
                Q(summary__icontains=query)
            )
            serializer = self.get_serializer(entries, many=True)
            return Response(serializer.data)
        return Response([])
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """按分类获取词条"""
        category_id = request.query_params.get('category_id')
        if category_id:
            entries = self.queryset.filter(categories__id=category_id)
            serializer = self.get_serializer(entries, many=True)
            return Response(serializer.data)
        return Response([])