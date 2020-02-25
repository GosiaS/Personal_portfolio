from django.shortcuts import render
from store.models import Product

def store_index(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "store_index.html", context)


