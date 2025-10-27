from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """词条分类模型"""
    name = models.CharField(max_length=100, verbose_name='分类名称')
    description = models.TextField(blank=True, verbose_name='分类描述')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Entry(models.Model):
    """百科词条模型"""
    title = models.CharField(max_length=200, verbose_name='词条标题')
    summary = models.TextField(blank=True, verbose_name='词条摘要')
    content = models.TextField(verbose_name='词条内容')
    categories = models.ManyToManyField(Category, blank=True, verbose_name='所属分类')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建者')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '词条'
        verbose_name_plural = '词条'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title