from django.db import models


class SiteSettings(models.Model):
    business_name = models.CharField(max_length=80)
    whatsapp = models.CharField(max_length=15)          # 254727277233 (no + or spaces)
    phone_display = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    hours = models.CharField(max_length=200, blank=True)
    map_link = models.URLField()
    map_query = models.CharField(max_length=200)
    delivery_zones = models.CharField(max_length=300)
    delivery_note = models.CharField(max_length=300)
    logo = models.ImageField(upload_to="site", blank=True)
    favicon = models.ImageField(upload_to="site", blank=True)

    class Meta:
        verbose_name_plural = "Site settings"

    def __str__(self):
        return self.business_name

    @classmethod
    def load(cls):
        return cls.objects.get_or_create(pk=1, defaults={
            "business_name": "Drips Lounge",
            "whatsapp": "254727277233",
            "phone_display": "0727 277 233",
            "address": "Mowlem Feroz, along Kangundo Road, Nairobi",
            "map_link": "https://maps.app.goo.gl/RHm51KZzp8iMJUQYA",
            "map_query": "Mowlem Feroz Kangundo Road Nairobi",
            "delivery_zones": "Umoja, Saika, Buruburu, Dandora and Komarock",
            "delivery_note": "Outside these areas, customers can arrange their own delivery.",
        })[0]


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=120)
    size = models.CharField(max_length=30, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)   # empty = "Ask for price"
    image = models.ImageField(upload_to="products", blank=True)
    tag = models.CharField(max_length=12, blank=True)            # e.g. HOT, NEW, DEAL
    available = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["category__order", "order", "name"]

    def __str__(self):
        return f"{self.name} {self.size}".strip()
