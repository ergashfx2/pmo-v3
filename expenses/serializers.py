from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseSummarySerializer(serializers.Serializer):
    name = serializers.CharField()
    count = serializers.IntegerField()