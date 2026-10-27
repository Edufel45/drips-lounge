from django.shortcuts import render
from django.templatetags.static import static
from .models import Product, SiteSettings


def index(request):
    site = SiteSettings.load()
    prods = Product.objects.filter(available=True).select_related("category")
    products = [[p.name, p.category.name, p.size, p.price, p.tag, p.image.url if p.image else ""] for p in prods]
    return render(request, "shop/index.html", {
        "site": site,
        "products": products,
        "cats": list(dict.fromkeys(p[1] for p in products)),
        "logo_url": site.logo.url if site.logo else static("img/logo.webp"),
        "lounge_url": static("img/lounge.webp"),
        "emblem_url": static("img/emblem.webp"),
        "favicon_url": site.favicon.url if site.favicon else static("img/favicon.png"),
    })
