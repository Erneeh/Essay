from django.contrib import admin
from .models import Membership, UserMembership, Subscription, Price, Kontaktai


class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]


admin.site.register(Membership, ProductAdmin)
admin.site.register(UserMembership)
admin.site.register(Subscription)
admin.site.register(Price)
admin.site.register(Kontaktai)