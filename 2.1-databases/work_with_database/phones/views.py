from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from phones.models import Phone


def index_view(request):
    return redirect('catalog')


def show_catalog_view(request):
    template = 'catalog.html'
    sort = request.GET.get("sort", "")

    phones = Phone.objects.all()

    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'min_price':
        phones = phones.order_by('price')
    elif sort == 'max_price':
        phones = phones.order_by('price')[::-1]

    context = {
        'phones': phones,
    }
    print(f'{sort}===>{phones}')
    return render(request, template, context)


def show_product_view(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)


def pageNotFound(request, exception):
    return HttpResponseNotFound(
        '<h1>Страница не найдена</h1>'
    )
