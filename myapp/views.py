from django.shortcuts import render
from myapp.models import contact
# Create your views here.

def base(request):
    return render(request, 'base.html')

def Contact(request):
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone') 
      msg = request.POST.get('msg')
      Contact = contact(name = name, email = email, phone = phone, msg = msg)
      Contact.save()
    return render(request, 'base.html')