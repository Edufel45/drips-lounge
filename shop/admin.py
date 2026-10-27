from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, SiteSettings

admin.site.site_header = "Drips Lounge Admin"
admin.site.site_title = "Drips Lounge"
admin.site.index_title = "Manage your shop"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("thumb", "name", "size", "category", "price", "available")
    list_display_links = ("thumb", "name")
    list_editable = ("price", "available")     # change prices / hide out-of-stock straight from the list
    list_filter = ("category", "available")
    search_fields = ("name",)
    list_per_page = 50

    @admin.display(description="Photo")
    def thumb(self, obj):
        return format_html('<img src="{}" style="height:40px">', obj.image.url) if obj.image else "-"


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
