from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ExpensesTracker.expenses.urls')),
    path('profile/', include('ExpensesTracker.profiles.urls')),
]
