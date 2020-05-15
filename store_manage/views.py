from django.db.models import Q
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView, TemplateView
from django.views.generic.detail import SingleObjectMixin

from store_manage.forms import CommentForm
from store_manage.models import StoreInformation, StoreComment


class StoreListView(ListView):
    template_name = 'store_manager/storelist.html'
    queryset = StoreInformation.objects.order_by('-top_star', '-modified_date')


class StoreDetailView(View):
    def get(self, request, *args, **kwargs):
        view = StoreDetailDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = StoreDetail.as_view()
        return view(request, *args, **kwargs)


class StoreDetail(FormView):
    """
    Post 数据处理保存
    """
    form_class = CommentForm

    def form_valid(self, form):
        sc = StoreComment()
        sc.content = form.cleaned_data['content']
        # sc.stor.store = form.cleaned_data['content']
        sc.store = StoreInformation.objects.get(code=self.kwargs.get('slug'))
        sc.store.save()
        sc.save()
        # form.store_id = self.kwargs.get('slug')
        # form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('detail', kwargs={'slug': self.kwargs.get('slug')})


class StoreDetailDisplay(DetailView):
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


class PopoverHtmlView(TemplateView):
    template_name = "store_manager/popover.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_comment'] = StoreInformation.objects.get(code=kwargs['slug']).storecomment_set.all()[:3]
        return context


class TopStar(View):

    def get(self, request, *args, **kwargs):
        slug = kwargs['slug']
        store = StoreInformation.objects.get(code=slug)

        if store.top_star == 1:
            store.top_star = 2
        else:
            store.top_star = 1
        store.save()

        data = {
            'code': slug,
            'top': store.top_star
        }
        return JsonResponse(data)
