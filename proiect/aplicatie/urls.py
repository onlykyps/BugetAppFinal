from django.urls import path

from aplicatie import views

app_name = 'transactions'

urlpatterns = [
    path('', views.TransactionsView.as_view(), name='transactions_list'),
    path('add_transaction/', views.CreateTransactionsView.as_view(), name='add'),
    path('incomes/', views.IncomesView.as_view(), name='incomes'),
    path('expenses/', views.ExpensesView.as_view(), name='expenses'),
    path('incomes_report/', views.IncomesReportView.as_view(), name='incomes_report'),
    path('expenses_report/', views.ExpensesReportView.as_view(), name='expenses_report'),
    path('<int:pk>/update/', views.UpdateTransactionsView.as_view(), name='update')
]
