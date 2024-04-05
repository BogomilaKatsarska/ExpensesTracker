from django.urls import path

from ExpensesTracker.profiles.views import profile_details, profile_edit, profile_delete, profile_create

urlpatterns = (
    path('', profile_details, name='profile details'),
    path('edit/', profile_edit, name='profile edit'),
    path('delete/', profile_delete, name='profile delete'),
    path('create/', profile_create, name='profile create'),
)