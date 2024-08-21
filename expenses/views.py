from datetime import datetime

from django.db.models import Sum
from django.db.models.functions import TruncMonth

from .utils import uzbek_month
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from expenses.models import Expense
from .serializers import ExpenseSerializer


class ExpensesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        expenses = Expense.objects.all().annotate(month=TruncMonth('date')).values('month').annotate(
            total_quantity=Sum('quantity')).order_by('month')
        formatted_expenses = [{"name": uzbek_month[expense['month'].month], "count": expense['total_quantity']} for
                              expense in expenses]
        return Response(formatted_expenses)


class CreateExpenseView(CreateAPIView):
    queryset = Expense.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer


class UpdateExpenseView(UpdateAPIView):
    queryset = Expense.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer


class DeleteExpense(DestroyAPIView):
    queryset = Expense.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer


class GetExpenseView(RetrieveAPIView):
    queryset = Expense.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer
