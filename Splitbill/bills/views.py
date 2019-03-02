from django.shortcuts import render
from .models import Bill


def index(request):
    return render(request, 'index.html')


def bill_entry(request):
    return render(request, 'bill_entry.html')


def bill_entry_submit(request):
    print("form is submitted.")

    name_bill = request.POST["name_bill"]
    amount = request.POST["amount"]
    description = request.POST["description"]
    date_bill = request.POST["date_bill"]
    bills = Bill(name_bill=name_bill, amount=amount, description=description, date_bill=date_bill)
    bills.save()

    return render(request, 'bill_entry.html')


def share_bill(request):
    return render(request, 'share_bill.html')


def monthly_bill(request):
    return render(request, 'monthly_bill.html')

