from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import News, Tag
from .serializers import NewsSerializer, TagsSerializer, NewsSerializerOps
from django_filters.rest_framework import DjangoFilterBackend


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'tags__name']

class NewsViewSetOps(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializerOps

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer