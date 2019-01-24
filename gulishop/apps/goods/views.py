from django.shortcuts import render
from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins, pagination, filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filter import GoodsFilter

# Create your views here.

class GoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = ('name', 'desc', 'goods_brief')
    ordering_fields = ('shop_price', 'sold_num')
    filter_class = GoodsFilter


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

    #def get_queryset(self):
    #    return GoodsCategory.objects.filter(category_type=1)



