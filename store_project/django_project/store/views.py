from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Value, F
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Product, Order
from .forms import SearchForm, ProductForm, UserRegistrationForm, LoginForm, OrderForm
from django.views.generic.base import TemplateView
# Create your views here.


def search(request):
    if request.method == 'GET':
        get_data = request.GET
        form = SearchForm(get_data)
        if form.is_valid():
            q = form.cleaned_data['q']
            products = Product.objects.filter(name__icontains=q).annotate(url_name=Value('author_detail'), obj_name=F('name'))
            object_list = list(products) 
            context = {'object_list': object_list}
            return render(request, 'new_app/search_list.html', context)


def product_list(request):
    posts = Product.objects.all()
    paginator = Paginator(posts, 1, orphans=1)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {"object_list": page.object_list, "page_obj": page}
    return render(request, "store/product_list.html", context)


class ProductCreate(CreateView):
    model = Product
    success_url = reverse_lazy('product_list')
    form_class = ProductForm


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    template_name = 'store/product_form.html'


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class ProductList(ListView):
    model = Product
    paginate_by = 2
    paginate_orphans = 1

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Bce продукты')
        return super().dispatch(request, *args, **kwargs)


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'


class MainPage(TemplateView):
    template_name = 'store/about.html'


class UserRegisterView(FormView, UserPassesTestMixin):
    template_name = 'store/product_form.html'
    form_class = UserRegistrationForm
    success_url = 'store/about.html'

    def post(self, request, *args, **kwargs):
        data = dict(request.POST)
        pass1 = data.pop('password1') # None
        pass2 = data.pop('password2') # None
        form = UserRegistrationForm(request.POST)
        if pass1 != pass2:
            return self.form_invalid(form)
        else:
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def form_valid(self, form):
        return HttpResponse('New user has been added')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.as_active:
                    login(request,user)
                    return HttpResponse('Authenticated succesfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'store/login.html', {'form': form})


class OrderCreate(CreateView):
    model = Order
    success_url = reverse_lazy('order_list')
    form_class = OrderForm


class OrderDetail(DetailView):
    model = Order
    context_object_name = 'order'


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
    template_name = 'store/order_form.html'


def order_list(request):
    posts = Order.objects.all()
    paginator = Paginator(posts, 1, orphans=1)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {"object_list": page.object_list, "page_obj": page}
    return render(request, "store/order_list.html", context)


class OrderList(ListView):
    model = Order
    paginate_by = 2

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Заказы')
        return super().dispatch(request, *args, **kwargs)
