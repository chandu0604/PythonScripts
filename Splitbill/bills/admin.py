from django.contrib import admin
from .models import Bill


class BillAdmin(admin.ModelAdmin):
    list_display = ('name_bill', 'amount', 'description', 'date_bill')


admin.site.register(Bill, BillAdmin)


