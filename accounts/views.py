from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView

from .forms import UserRegistrationForm
from .models import EmployeeProfile


def all_users(request):
    all_employees = EmployeeProfile.objects.all()
    context = {
        "employees" : all_employees
    }
    return render(request, 'accounts/list.html', context)

def user_details(request, id):
    employee = get_object_or_404(EmployeeProfile, pk=id)
    context = {
        "employee" : employee
    }
    return render(request, 'accounts/details.html', context)


class AuthLogin(LoginView):
    template_name = 'accounts/login.html'


def register_user_view(request):
    if request.user:
        form = UserRegistrationForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect(reverse('home'))

        context = {
            "form" : form
        }
        return render(request, 'accounts/register.html', context)
    else:
        return redirect(reverse('home'))