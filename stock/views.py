from django.views.generic import ListView
from stock.models import Part


class UncontainedPartsView(ListView):
    model = Part
    queryset = Part.objects.filter(part_container__isnull=True)
    context_object_name = 'uncontained_parts'
    template_name = 'stock/uncontained_parts.html'
    paginate_by = 20