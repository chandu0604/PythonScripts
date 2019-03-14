from django.contrib import admin
from .models import Bill, Share


class BillAdmin(admin.ModelAdmin):
    list_display = ('name_bill', 'amount', 'description', 'date_bill')


admin.site.register(Bill, BillAdmin)


class ShareAdmin(admin.ModelAdmin):
    list_display = ('name_shared', 'amount_shared')


admin.site.register(Share, ShareAdmin)


