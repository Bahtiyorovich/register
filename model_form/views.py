from django.shortcuts import render, redirect
from .form import CustomerForm
from .models import Customer

# Create your views here.

def sign_up(request):
    form = CustomerForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect('customers_list')

    ctx = {'form': form}

    return render(request, 'signup.html', ctx)

def customers_list(request):
    customers = Customer.objects.all()
    ctx = {'customers': customers}
    return render(request, 'customers_list.html', ctx)