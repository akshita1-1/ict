from django.shortcuts import HttpResponse , render , redirect
from fries_app.models import test

def home(request):
    return render(request,'home.html')

from django.shortcuts import HttpResponse , render

def menu(request):

    return render(request,'menu.html')

from django.shortcuts import HttpResponse , render

def checkout(request):
    data= test.objects.all()   #getting all the data from the table to django

    if request.method == 'POST':
        var1 = request.POST.get('name')
        var2 = request.POST.get('number')
        
        test_instance=test(name=var1,number=var2)
        test_instance.save()
        return redirect('home')
    

    return render(request,'checkout.html', {'data':data})