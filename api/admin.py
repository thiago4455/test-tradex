from django.contrib import admin
from api.models import Product, Price

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('ean', 'name', 'min_price', 'max_price', 'image',)
    search_fields = ('ean', 'name',)
    
    change_form_template = "admin/custom_pages/product.html"

class PriceAdmin(admin.ModelAdmin):
    autocomplete_fields = ('product',)
    list_display = ('product', 'price', 'created_at',)
    readonly_fields = ('created_at',)
    search_fields = ("product__ean",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)