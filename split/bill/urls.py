from django.urls import path, utils
from . import views

urlpatterns = [
    path('', views.index),
    path('bill_entry/', views.bill_entry),
    path('bill_entry_submit', views.bill_entry_submit),
    path('total_bills/', views.total_bills),
    path('total_bills_delete_person/<int:id>', views.total_bills_delete_person),
    path('share_bill/', views.share_bill),
    path('share_bill_submit', views.share_bill_submit),
    path('share_bill_submit_evaluate', views.share_bill_submit_evaluate),
    path('delete_person/<int:id>', views.delete_person)

]
