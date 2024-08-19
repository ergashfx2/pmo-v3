from rest_framework.generics import CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from expenses.models import Expense
from .serializers import ExpenseSerializer

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

