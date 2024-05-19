from django.forms import forms
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from aplicatie.models import Transactions
from django import forms


# Create your views here.

class TransactionsView(ListView):
    model = Transactions
    template_name = 'aplicatie/transactions_index.html'


class CreateTransactionsView(CreateView):
    model = Transactions
    fields = ['date', 'account', 'amount', 'note', 'type']
    template_name = 'aplicatie/transactions_form.html'

    def get_success_url(self):
        return reverse('transactions:transactions_list')

    # def get_form(self):
    #     """add date picker in forms"""
    #     form = super(CreateTransactionsView, self).get_form()
    #     form.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date'})
    #     return form


class IncomesView(ListView):
    model = Transactions
    template_name = 'aplicatie/incomes.html'


class ExpensesView(ListView):
    model = Transactions
    template_name = 'aplicatie/expenses.html'


class IncomesReportView(ListView):
    model = Transactions
    template_name = 'aplicatie/incomes_report.html'


class ExpensesReportView(ListView):
    model = Transactions
    template_name = 'aplicatie/expenses_report.html'


class UpdateTransactionsView(UpdateView):
    model = Transactions
    fields = ['date', 'account', 'amount', 'note', 'type', 'active']
    template_name = 'aplicatie/transactions_form.html'

    def get_success_url(self):
        return reverse('transactions:transactions_list')


def delete_transaction(request, pk):
    Transactions.objects.filter(id=pk).update(active=False)
    return redirect('transactions:transactions_list')


def activate_transaction(request, pk):
    Transactions.objects.filter(id=pk).update(active=True)
    return redirect('transactions:transactions_list')
