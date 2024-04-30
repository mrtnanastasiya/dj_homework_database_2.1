from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sort_conversion = {
        "name": "name",
        "min_price": "price",
        "max_price": "-price",
    }

    sort_type = request.GET.get("sort", "name")
    # print(sort_type)
    dj_sort_type = sort_conversion[sort_type]
    # print(dj_sort_type)
    phones = Phone.objects.all().order_by(dj_sort_type)
    context = {
        "phones": phones
    }
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)

    context = {
        "phone": phone
    }

    print("перем slug = ", slug)
    return render(request, template, context)
