from django_filters.rest_framework import DjangoFilterBackend

class NotDeletedObjects(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        qs = super().filter_queryset(request, queryset, view)
        if 'deleted' in request.query_params:           # If deleted in query_params
            return qs.filter(deleted_at__isnull=False)  # show deleted objects
        return qs.filter(deleted_at__isnull=True)       # otherwise show not deleted objects