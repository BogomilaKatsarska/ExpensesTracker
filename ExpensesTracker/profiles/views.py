from django.shortcuts import render, redirect

from ExpensesTracker.profiles.forms import ProfileForm


def profile_details(request):
    pass


def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def profile_edit(request):
    pass


def profile_delete(request):
    pass
