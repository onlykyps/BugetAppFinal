from django.contrib.auth.decorators import login_required, permission_required
from django.forms import forms
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from aplicatie.models import Transactions
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here. 'LoginRequiredMixin'?

class TransactionsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Transactions
    template_name = 'aplicatie/transactions_index.html'
    permission_required = 'transactions.view_transactions'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     data = super(TransactionsView, self).get_context_data(**kwargs)
    #     return data


class CreateTransactionsView(LoginRequiredMixin, CreateView):
    model = Transactions
    fields = ['date', 'account', 'amount', 'note', 'subcategory', 'type']
    template_name = 'aplicatie/transactions_form.html'

    def get_success_url(self):
        return reverse('transactions:transactions_list')

    # def get_form(self):
    #     """add date picker in forms"""
    #     form = super(CreateTransactionsView, self).get_form()
    #     form.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date'})
    #     return form


class IncomesView(LoginRequiredMixin, ListView):
    model = Transactions
    template_name = 'aplicatie/incomes.html'


class ExpensesView(LoginRequiredMixin, ListView):
    model = Transactions
    template_name = 'aplicatie/expenses.html'


class IncomesReportView(LoginRequiredMixin, ListView):
    model = Transactions
    template_name = 'aplicatie/incomes_report.html'


class ExpensesReportView(LoginRequiredMixin, ListView):
    model = Transactions
    template_name = 'aplicatie/expenses_report.html'


class UpdateTransactionsView(LoginRequiredMixin, UpdateView):
    model = Transactions
    fields = ['date', 'account', 'amount', 'note', 'type', 'active']
    template_name = 'aplicatie/transactions_form.html'

    def get_success_url(self):
        return reverse('transactions:transactions_list')


@login_required
def delete_transaction(request, pk):
    Transactions.objects.filter(id=pk).update(active=False)
    return redirect('transactions:transactions_list')


@login_required
# @permission_required()
def activate_transaction(request, pk):
    Transactions.objects.filter(id=pk).update(active=True)
    return redirect('transactions:transactions_list')
