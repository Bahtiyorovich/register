from django.shortcuts import render
from .models import User
# Create your views here.


def register(request):
    if request.POST:
        model = User()
        model.first_name = request.POST.get('first_name', '')
        model.last_name = request.POST.get('last_name', '')
        model.email = request.POST.get('email', '')
        model.company = request.POST.get('company', '')
        model.phone_number = request.POST.get('phone_number', '')
        model.subject = request.POST.get('subject', '')
        model.exist = request.POST.get('exist', '')
        model.save()
    return render(request, 'auth.html')