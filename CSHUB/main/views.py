from django.http import HttpResponse
import collections as c
import json
from bson.json_util import dumps, loads
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .models import Resource
from django.db import connection
cursor = connection.cursor()
from django.contrib.auth import logout

# Create your views here.

def home(request):
    if 'user' in request.session:
        user_email = request.session['user']
        try:
            user_db = User.objects.get(email=user_email)
        except:
            return render(request, './error.html')
        print(f'user is now {user_db}')
        fname = user_db.first_name
        param = {
            'name': fname
        }
        return render(request, './index.html', param)
    return render(request, './index.html')


def signin(request):
    if request.method == 'POST':
        # first retrieve fields entered by user
        useremail = request.POST['email']
        userpassword = request.POST['password']
        print(f'email entered is {useremail} password entered is {userpassword}')
        try:
            email_db = User.objects.get(email=useremail)
        except:
            return render(request, './error.html')
        if email_db:
            # email exists - now check the password
            if useremail == email_db.email and userpassword == email_db.password:
                # user authenticated
                request.session['user'] = useremail
                print(email_db.first_name)
                fname = email_db.first_name
                lname = email_db.last_name
                print(fname)
                print(lname)
                info = {
                    'name': fname,
                    'lname': lname
                }
                return render(request, './index.html', info)
            else:
                return render(request, './error.html')
        else:
            return render(request, './error.html')

    return render(request, './signin.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        useremail = request.POST['email']
        userpassword = request.POST['password']
        userObject = {
            'email': useremail,
            'password': userpassword,
            'resource_history': 'NULL',
            'resources_added': 'NULL',
            'first_name': fname,
            'last_name': lname
        }
        print(f'email entered is {useremail} password entered is {userpassword}')
        flag = 0
        try:
            edb = User.objects.all()
        except:
            return render(request, './error.html')
        # check if email exists or not
        for e in edb:
            if useremail==e.email:
                flag = 1
                print('Email exists')
        print('email does not exist')
        # result = {User.objects.filter(email=edb)}

        print(f'flag is {flag}')
        if flag == 1:
            return render(request, './error.html')
        else:
            # otherwise the user has signed up, take them to login page
            # insert user in the database
            # indicates that a user already is registered - display an error page
            print(f'The email that should be registered {useremail} and password {userpassword}')
            # all new users initially register with a null value in resources_added
            # and resource history
            # The user id should self increment - serialized
            u = User(first_name=fname, last_name=lname, email=useremail, password=userpassword, resource_history="null", resources_added="null")
            u.save()
            info = {
                'name': fname,
                'lname': lname
            }
            return render(request, './signin.html', info)
    return render(request, './signup.html')


def logout(request):
    try:
        del request.session['user']
        logout(request)
    except:
        return redirect('signin')
    return redirect('signin')


def searchResults(request):
    if 'user' in request.session:
        useremail = request.session['user']
        try:
            res = Resource.objects.all()
            res_count = Resource.objects.all().count()
            user = User.objects.get(email=useremail)
            user2 = User.objects.get(user_id=res[0].uid_id)
            print(user2.email)
            print(res[0].uid_id)
        except:
            print('Error with fetching of resources')
            return render(request, './error.html')
        fname = user.first_name
        result = {
            'name': fname,
            'count': res_count,
            'resources': res
        }
        return render(request, './searchResults.html', result)
    return render(request, './error.html')


def addPage(request):
    if 'user' in request.session:
        return render(request, './add.html')
    return render(request, './error.html')

def add(request):
    # make sure the page is only accessible to users
    # else render an error page
    if 'user' in request.session:
        print('Inside add')
        if request.method == 'POST':
            # enable the user to add a resource
            try:
                resource_db = Resource.objects.all()
            except:
                print('Error fetching resources')
                return render(request, './error.html')
            # # should contain all the resources in resource table
            print('Resources table: ')
            print(resource_db)
            # extract the values from the addition form


            # try:
            u_category = request.POST['category']
            u_title = request.POST['title']
            u_description = request.POST['description']
            print('Gonna print some values now: ')
            print(u_category)
            print(u_title)
            print(u_description)
            # except:
            #     return render(request, './error.html')

            try:
                user_email = request.session['user']
                try:
                    u_result = User.objects.get(email=user_email)
                    print(f'User result is {u_result}')
                except:
                    print('Error fetching user')
                    return render(request, './error.html')

                save_user_id = u_result.user_id
                print(f'Saved user id is {save_user_id}')

                rec = Resource(category=u_category, title=u_title, uid=u_result, description=u_description)
                rec.save()
                print('Resource has been added')
            except:
                print('Error adding resource')
                return render(request, './error.html')

            user_email = request.session['user']
            try:
                user_db = User.objects.get(email=user_email)
            except:
                print('Error in user')
                return render(request, './error.html')
            print(f'user is now {user_db}')
            fname = user_db.first_name
            param = {
                'name': fname
            }
            return render(request, './add.html', param)

    return render(request, './error.html')

