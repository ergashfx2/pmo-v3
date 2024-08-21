from django.urls import path
from .views import *

urlpatterns = [
    path('all/',ExpensesView.as_view(),name='all-expenses-view'),
    path('<pk>',GetExpenseView.as_view(),name='all-expenses'),
    path('create/',CreateExpenseView.as_view(),name='create-expense'),
    path('update/<pk>',UpdateExpenseView.as_view(),name='update-expense'),
    path('delete/<pk>',DeleteExpense.as_view(),name='delete-expense'),
]