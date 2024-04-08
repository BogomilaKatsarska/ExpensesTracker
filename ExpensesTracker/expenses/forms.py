from django import forms
from django.core.exceptions import ValidationError

from ExpensesTracker.core.profile_utils import get_profile
from ExpensesTracker.expenses.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


    def clean_price(self):
        budget_left = get_profile().budget_left
        if budget_left < float(self.cleaned_data['price']):
            raise ValidationError('Not enough budget')


class CreateExpenseForm(ExpenseForm):
    pass


class EditExpenseForm(ExpenseForm):
    pass


class DeleteExpenseForm(ExpenseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     if commit:
    #         instance.delete()
    #     return instance
