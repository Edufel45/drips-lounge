import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="SiteSettings",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("business_name", models.CharField(max_length=80)),
                ("whatsapp", models.CharField(max_length=15)),
                ("phone_display", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=200)),
                ("hours", models.CharField(blank=True, max_length=200)),
                ("map_link", models.URLField()),
                ("map_query", models.CharField(max_length=200)),
                ("delivery_zones", models.CharField(max_length=300)),
                ("delivery_note", models.CharField(max_length=300)),
                ("logo", models.ImageField(blank=True, upload_to="site")),
                ("favicon", models.ImageField(blank=True, upload_to="site")),
            ],
            options={"verbose_name_plural": "Site settings"},
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=60, unique=True)),
                ("order", models.PositiveSmallIntegerField(default=0)),
            ],
            options={"verbose_name_plural": "categories", "ordering": ["order", "name"]},
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("size", models.CharField(blank=True, max_length=30)),
                ("price", models.PositiveIntegerField(blank=True, null=True)),
                ("image", models.ImageField(blank=True, upload_to="products")),
                ("tag", models.CharField(blank=True, max_length=12)),
                ("available", models.BooleanField(default=True)),
                ("order", models.PositiveSmallIntegerField(default=0)),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="products", to="shop.category")),
            ],
            options={"ordering": ["category__order", "order", "name"]},
        ),
    ]
