from django.shortcuts import render, redirect

from ExpensesTracker.core.profile_utils import get_profile
from ExpensesTracker.expenses.models import Expense
from ExpensesTracker.profiles.forms import CreateProfileForm, EditProfileForm


def profile_details(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget = profile.budget
    budget_left = budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'budget_left': budget_left,
        'budget': budget,
    }
    return render(request, 'profile.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Expense.objects.all().delete()
        return redirect('index')

    context = {
    }

    return render(request, 'profile-delete.html', context)