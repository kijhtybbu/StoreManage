from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from store_manage.forms import CommentForm
from store_manage.models import StoreInformation


class StoreListView(ListView):
    template_name = 'store_manager/storelist.html'
    queryset = StoreInformation.objects.order_by('-Opening_date')


class StoreDetailView(DetailView):
    model = StoreInformation
    template_name = 'store_manager/detail.html'
    slug_field = 'code'
    # slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = CommentForm()
        return context


class StoreCreate(CreateView):
    model = StoreInformation
    template_name = 'store_manager/store_create_form.html'
    fields = ['name']


class StoreUpdate(UpdateView):
    model = StoreInformation
    slug_field = 'code'
    slug_url_kwarg = 'slug'
    fields = ['name', 'code', 'brand', 'address', 'IP', 'ap', 'contacts']
    template_name = "store_manager/detail.html"
