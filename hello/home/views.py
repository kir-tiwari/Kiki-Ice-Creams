# from django.shortcuts import render,HttpResponse
#
# # Create your views here.
#
# def index(request):
#     return HttpResponse("This is Home Page")

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from django.contrib import messages
from .models import Contact

def index(request):
    context={
        'variable':"this is sent",
        'var1':'HELLO',
        'var2':'HOLA'
    }
    # messages.success(request,"This is a test message")
    return render(request,'index.html',context)
    # return HttpResponse("This is Home Page")

def about(request):
    return HttpResponse("This is About Page")

def services(request):
    return HttpResponse("This is Services Page")

def contact(request):
    if (request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        # datetime.today()
        contact_ = Contact(name = name, email = email , phone = phone, comment = comment , date=datetime.today())
        contact_.save()
        messages.success(request,'Your message has been sent')
        # return render(request, 'contact.html', {'message': 'Thanks for contacting us!'})
    return render(request, 'contact.html')