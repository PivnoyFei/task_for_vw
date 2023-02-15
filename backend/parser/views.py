import asyncio
from parser.filters import NewsFilterSet
from parser.models import News, Tag
from parser.pagination import CustomPagination
from parser.parser import telegram_parser
from parser.serializers import (NewsCreateSerializer, NewsSerializer,
                                TagSerializer)

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminUser,)
    pagination_class = CustomPagination


class NewsViewSet(ModelViewSet):
    """Выдает новости с панигпцией, доступен фильтр по тегам."""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminUser,)
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = NewsFilterSet

    def get_serializer_class(self):
        if self.request.method in ("POST", ):
            return NewsCreateSerializer
        return NewsSerializer

    def create(self, request):
        """Укажите тег и функция спарсит данные по ссылке из тега."""
        tag = request.data.get('tags', None)
        teg = get_object_or_404(Tag, name=tag)
        asyncio.run(telegram_parser(teg))
        return Response(status=status.HTTP_201_CREATED)
