from datetime import date
from pickle import NONE
import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

from xafari.models import user_details
from xafari.models import places

# Create your views here.
def home(request):
    return render(request, "home.html")
def form1(request):
    return render(request, "form1.html")





# Create your views here.
def register(request):

    if request.method == 'POST':
        firstname=request.POST['firstname']
        secondname=request.POST['secondname']
        username=request.POST['username']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        email=request.POST['email']
        
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken!!!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken!!')
                return redirect('register')
            else:    
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=firstname, last_name=secondname )#creating object for saving in database
                user.save();
                messages.info(request,'user created!')
                return redirect('login')
                
               
        else:
            messages.info(request,"password didn't matched")
            return redirect('register')
           
       
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['passw']

        use=auth.authenticate(username=username, password=password)
        if use is not NONE:
            auth.login(request,use)
            return redirect('/')
        else:
            messages.error(request,'inlid credintials')
            return redirect('login')
    else:
        return render(request,'login.html')
    

def form1(request):
        return render(request,'form1.html')
def new(request):
    if request.method == 'POST':
        if request.POST.get('number') and request.POST.get('from_place') and request.POST.get('to_place') and request.POST.get('number_of_passengers') and request.POST.get('arrival_date') and request.POST.get('leaving_date'):
            saverecord = user_details()
            saverecord.number = request.POST.get('number')
            saverecord.from_place = request.POST.get('from_place')
            saverecord.to_place = request.POST.get('to_place')
            saverecord.number_of_passengers = request.POST.get('number_of_passengers')
            saverecord.arrival_date = request.POST.get('arrival_date')
            saverecord.leaving_date = request.POST.get('leaving_date')
            saverecord.save()
            messages.info(request,'Order booked')
            return render(request,'home.html')
    else:
            messages.info(request,'cant book')
            return render(request,'form1.html')

  

    #if request.method=='POST':
    #    number = request.POST.get['number']
     #   from_place = request.POST.get['from_place']
     #   to_place = request.POST.get['to_place']
     #   numberpass = request.POST.get['number_of_passengers']
      #  arrival_date = request.POST.get['arrival_date']
       # leaving_date=  request.POST.get['leaving_date']

      #  details = user_details(number=number, from_place=from_place, to_place=to_place, number_of_passengers=numberpass, arrival_date=arrival_date, leaving_date=leaving_date)
     #   details.save()
      #  messages.info(request, 'Order placed Mr' )
       # return redirect('/')
        #else:
         #   return render(request,'form1.html')
   # else:
    #    messages.info(request, 'Cant place the order' )
     #   return render(request,'form1.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def technology(request):
    return render(request, "technology.html")

def about(request):
    return render(request, 'about.html')


def book(request):
    place=places.objects.all()
    return render(request, "book.html", {'place' : place})    
