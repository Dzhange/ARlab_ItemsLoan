# encode:utf-8

from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse, Http404
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *


ADMIN = ('YangTheBoss','Django','Aoliao')

# Create your views here.
def index(request):
    # User has to login then view the site
    if not request.user.is_authenticated:
        return HttpResponseRedirect('borrow/login')
    else:
        user = request.user
        if user.username not in ADMIN:
            context = {
                'stuff_type':STUFF_NAME,
                'room_type': ROOM_LIST,
            }
            if request.method == 'POST':
                info = request.POST
                print(info)
                
            return render(request,'homepage.html',context)
        return render(request, 'borrow/administration.html')

def Homepage(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect('borrow/login')
    else:
        context = {
            'stuff_type':STUFF_NAME,
            'room_type': ALL_ROOM,
        }
        form = BorrowRecordForm(request.POST or None)  
        print(request.POST)
        if form.is_valid():
            raw_record = form.save(commit = False)
            raw_record.borrower = request.user
            return HttpResponseRedirect('/borrow')
        context = {
            "form": form,
            "all_user" : User.objects.all(),
        }
        return render(request, 'book/add_book.html', context)          

def BorrowRequest(request, book_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('borrow/login')
    else:    
        user = request.user
        form = BorrowRecordForm(request.POST or None, request.FILES or None)
        if form.is_valid(): 
            record = form.save(commit=False)
            record.borrower = request.user
            record.save()
            return HttpResponseRedirect("/borrow/%d/history" % user.id)
        context = {
            "ErrorMessage":"FORM ERROR : FORM UPLOADED IS NOT VALID"
        }
        return render(request,'borrow/',context)


def PersonalHistory(request,user_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('borrow/login')
    else:
        if request.user.id != user_id:
            return HttpResponse(status = 403)
        else:
            context = {
                'user' : request.user,
            }
            return render(request,'borrow/personalhistory.html',context)


def AllHistory(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/borrow')
    else:
        if request.user.username in ADMIN:
            PerformedLoan = BorrowRequest.objects.filter(is_approved = True)
            context = {
                'all_records':PerformedLoan
            }
            return render(request,'borrow/allhistory.html',context)
        return render(request,'borrow/')

"""
Functions related to user authentication
"""
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'borrow/homepage.html')

    context = {
        "form": form,
    }
    return render(request, 'book/register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.username in ADMIN:
                return HttpResponseRedirect('borrow/administration')
            return HttpResponseRedirect('borrow/homepage')
        else :
            return render(request, 'borrow/login.html')
    else:
        return render(request, 'borrow/login.html')

def logout(request):
    if not request.user.is_authenticated:
        return render(request, 'borrow/login.html')
    else:
        return render(request, 'borrow/homepage_guest.html')