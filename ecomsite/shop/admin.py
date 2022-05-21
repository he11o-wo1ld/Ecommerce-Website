from django.contrib import admin
from .models import *


admin.site.site_header = "E-Comerece Site"
admin.site.site_title = "Online Shopping"
admin.site.index_title = "Shopping"


class ProductAdmin(admin.ModelAdmin):
    def changeCategoryToDefault(self, request, queryset):
        queryset.update(category="Default")

    changeCategoryToDefault.short_description = 'Default Category'
    list_display = ('title', 'price', 'discountPrice', 'category', 'description', 'image',)
    search_fields = ('title', 'category','description',)
    actions = ('changeCategoryToDefault',)
    fields = ('title', 'price', 'discountPrice', 'category', 'description', 'image',)
    list_editable = ('price', 'discountPrice', 'category', 'description','image')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'address', 'city', 'state', 'zipcode', 'total')
    search_fields = ('items', 'name', 'email', 'address', 'city', 'state', 'zipcode', 'total')
    actions = ('changeAddressToDefault',)
    list_editable = ('name', 'email', 'address', 'city', 'state', 'zipcode',)

    def changeAddressToDefault(self, request, queryset):
        queryset.update(address='')


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
