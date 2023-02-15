from parser.models import News, Tag

from django_filters import FilterSet, filters


class NewsFilterSet(FilterSet):
    """Фильтр для новостей."""
    pub_date = filters.DateFromToRangeFilter()
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags__name',
        queryset=Tag.objects.all(),
        to_field_name='name',
    )

    class Meta:
        model = News
        fields = ('pub_date', 'tags')
