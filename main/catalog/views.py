from django.shortcuts import render
from main.catalog.models import Product


# Create your views here.

def home(request):
    product_list = Product.objects.all()
    context = {
        'product': product_list,
        "title": "Главная",
    }
    return render(request, "catalog/home.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("massage")
        print(f"{name}\n{email}\n{massage}")
    context = {
        "title": "Контакты",
    }
    return render(request, "catalog/contacts.html", context)

def catalog(request, pk):
    context = {
        'product': Product.objects.filter(id=pk),
        "title": "Главная",
    }
    return render(request, "catalog/products_detail.html", context)
