from parser.views import NewsViewSet, TagViewSet

from django.urls import include, path
from rest_framework.routers import SimpleRouter

app_name = 'api'

router = SimpleRouter()
router.register('tags', TagViewSet, 'tags')
router.register('news', NewsViewSet, 'news')


urlpatterns = [
    path('', include(router.urls)),
]
