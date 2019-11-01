from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from store_manage.models import StoreInformation


class StoreListView(ListView):
    template_name = 'storelist.html'
    queryset = StoreInformation.objects.order_by('-Opening_date')

    # def get_queryset(self):
    #     # self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
    #     search_text = self.kwargs['search_text']
    #     # return StoreInformation.objects.filter(Q(name__contains=search_text) | Q(code__contains=search_text))
    #     return StoreInformation.objects.filter(Q(name__contains=search_text) | Q(code__contains=search_text))

class StoreDetailView(DetailView):
    model = StoreInformation
    template_name = 'detail.html'