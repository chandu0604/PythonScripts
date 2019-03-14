from django.db.models import Sum
from django.shortcuts import render
from .models import Bill, Share
from .apps import split_the_bill


def index(request):
    return render(request, 'index.html')


def bill_entry(request):
    return render(request, 'bill_entry.html')


def bill_entry_submit(request):
    try:
        name_bill = request.POST["name_bill"]
        amount = request.POST["amount"]
        description = request.POST["description"]
        date_bill = request.POST["date_bill"]
        bills = Bill(name_bill=name_bill, amount=amount, description=description, date_bill=date_bill)
        bills.save()
    except ValueError:
        pass
    return render(request, 'bill_entry.html')


def total_bills(request):
    total = Bill.objects.all()
    total_amounts = Bill.objects.aggregate(Sum('amount'))
    total_amount = total_amounts['amount__sum']
    print(total_amount)
    return render(request, 'total_bills.html', {'total': total, 'total_amount': total_amount})


def total_bills_delete_person(request, id):
    query = Bill.objects.get(id=id)
    query.delete()
    total = Bill.objects.all()
    total_amounts = Bill.objects.aggregate(Sum('amount'))
    total_amount = total_amounts['amount__sum']
    return render(request, 'total_bills.html', {'total': total, 'total_amount': total_amount})


def share_bill(request):
    share = Share.objects.all()
    return render(request, 'share_bill.html', {'share': share})


def share_bill_submit(request):
    try:
        name_shared = request.POST["name_shared"]
        amount_shared = request.POST["amount_shared"]
        shared_bill = Share(name_shared=name_shared, amount_shared=amount_shared)
        shared_bill.save()
    except ValueError:
        pass
    share = Share.objects.all()
    return render(request, 'share_bill.html', {'share': share})


def delete_person(request, id):
    query = Share.objects.get(id=id)
    query.delete()
    share = Share.objects.all()
    return render(request, 'share_bill.html', {'share': share})


def share_bill_submit_evaluate(request):
    share_set = Share.objects.values('name_shared', 'amount_shared')
    list_result = [entry for entry in share_set]
    new_dict = {item['name_shared']: item['amount_shared'] for item in list_result}
    total_share = split_the_bill(new_dict)
    return render(request, 'share_bill_evaluate.html', {'total_share': total_share})



