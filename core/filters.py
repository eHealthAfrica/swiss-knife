import django_filters

from models import Event

class EventFilter(django_filters.FilterSet):
    after = django_filters.DateTimeFilter(name='modified_at', lookup_type='gte')
    code = django_filters.CharFilter(name='event_t__code')

    class Meta:
        model=Event
        fields = ['after', 'code']