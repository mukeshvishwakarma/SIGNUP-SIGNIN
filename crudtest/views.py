from django.shortcuts import render, redirect
from django.contrib import messages
from crudtest.models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def forpass(request):
    return render(request, 'forpass.html')


def UserReg(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        State = request.POST['State']
        city = request.POST['city']
        mobile_no = request.POST['mobile_no']

        if CustomUser.objects.filter(candidate_id=username).exists():
            messages.error(request, 'Username already taken...')
            return redirect('UserReg')
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exist....')
            return redirect('UserReg')
        else:
            CustomUser(
                candidate_id=username, email=email, state=State, city=city, first_name=fname, last_name=lname, mobile_no=mobile_no, password=email).save()

            # user.groups.add(user_group)
            return redirect('user_login')  # customerLogin
            # return HttpResponse("user create")
    else:
        pass
    return render(request, 'user_register.html')


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        myuser = CustomUser.objects.filter(
            Q(candidate_id=username) & Q(password=password))
        print('myuser', myuser)
        if myuser is not None:
            return render(request, 'dashboard.html')
        else:
            messages.error(request, 'Invalid Username OR password')
            return redirect('user_login')
    return render(request, 'user_login.html')


def signout(request):
    messages.success(request, "Logged Out Successfully!")
    return redirect('user_login')
