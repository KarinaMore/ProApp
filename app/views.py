from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image
from io import BytesIO
from django.conf import settings
import base64, os
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
import uuid
from .models import Registration
from django.urls import reverse_lazy

from django.contrib import messages
import random
import string
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string





# Create your views here.
def home(request):
    return render(request, 'home.html')


def registration_user(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        middle_name= request.POST.get('middle_name')
        mobile= request.POST.get('mobile')
        address= request.POST.get('address')
        email= request.POST.get('email')
        image = request.FILES.get('image')
        company_name= request.POST.get('company_name')
        company_register_no= request.POST.get('company_register_no')
        company_email= request.POST.get('company_email')
        company_mobile= request.POST.get('company_mobile')
        company_address= request.POST.get('company_address')
        company_incorporation=request.FILES.get('company_incorporation')
        pan_card= request.FILES.get('pan_card')
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        ctx = {
           'username' : username,
           'password' : password,
           'first_name':first_name,
           'last_name':last_name,
        }
        message = render_to_string('mail.html', ctx)
        
        send_mail(
        'User Info',
        message,
        settings.EMAIL_HOST_USER,
        [company_email], 
        fail_silently=False, html_message=message)

        if password != confirm_password:
            return render(request, 'registration_user.html', {'error': 'Passwords do not match'})

        # Save the user login information if passwords match
        registration_user = Registration.objects.create(user_name=username, password=password,confirm_password=confirm_password,first_name=first_name,last_name=last_name,email=email,address=address,middle_name=middle_name,mobile=mobile,image=image,company_name=company_name,company_register_no=company_register_no,company_email=company_email,company_mobile=company_mobile,company_address=company_address,company_incorporation=company_incorporation,pan_card=pan_card)
        user = User.objects.create_user(username=username,password=password)
        registration_user.save()
        user.save()

        return redirect('success')  # Redirect to home page after successful registration

    return render(request, 'registration_form.html')



def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(username=user_name, password=password)

        if user is not None:
            # If user is authenticated, log them in
            login(request, user)
            return redirect('menu_card')
        else:
            # If authentication fails, you might want to handle the error here
            # For example, render the login form again with an error message
            return render(request, 'user_login.html', {'error': 'Invalid username or password'})

    return render(request, 'user_login.html')



def agent_page(request):
    if request.method == 'POST':
        first_name1 = request.POST.get('first_name1')
        middle_name2 = request.POST.get('middle_name2')
        last_name3 = request.POST.get('last_name3')
        mobile1 = request.POST.get('mobile1')
        email1 = request.POST.get('email1')
        aadhar1 = request.FILES.get('aadhar1')
        photo1 = request.FILES.get('photo1')

        # Generate a 4-digit UUID
        unique_id = str(uuid.uuid4())[:4]

        agent_page = AgentReg.objects.create(first_name1=first_name1, middle_name2=middle_name2, last_name3=last_name3, mobile1=mobile1, email1=email1, aadhar1=aadhar1, photo1=photo1, unique_id=unique_id)
        
        agent_page.save()

        return redirect('menu_card')
        
    return render(request, 'agent_page.html')



def menu_card(request):
    agent = AgentReg.objects.all()

    context ={
        'manage_agent':agent
    }
    return render(request, 'menu_card.html',context)




def help_hire_view(request):
    if request.method == 'POST':
        help_name = request.POST.get('help_name')
        help_email =request.POST.get('help_email')
        help_company_name_help =request.POST.get('help_company_name_help')
        subject_help2 =request.POST.get('subject_help2')
        select_department_help =request.POST.get('select_department_help')
        your_massage_help =request.POST.get('your_massage_help')

        help_hire_view =HelpHire.objects.create(help_name=help_name, help_email=help_email, help_company_name_help=help_company_name_help, subject_help2=subject_help2, select_department_help=select_department_help,  your_massage_help=your_massage_help)

        help_hire_view.save()

        return redirect('home')

    return render(request, 'help_hire.html')


def manage_agent(request):
    agent = AgentReg.objects.all()

    context ={
        'manage_agent':agent
    }

    return render(request, 'manage_agent.html', context)


def leadpanel_tab(request):
    agent = AgentReg.objects.all()

    context ={
        'manage_agent':agent
    }
    return render(request, 'leadpanel_tab.html',context)


def success(request):
    return render(request, 'success.html')


def delete(request,id):
    agent=AgentReg.objects.get(id=id)
    agent.delete()

    return redirect('manage_agent')


def view_profile(request):
    username=request.user.username
    profiles = Registration.objects.filter(user_name=username)
    context = {
        'profiles': profiles
    }
    return render(request, 'view_profile.html', context)


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('home'))



def get_random_number_string(length):
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))


@login_required
def change_username(request):
    employee = Registration.objects.get(user_name=request.user.username)

    if request.method == 'POST':
        new_username = request.POST.get('new_username')
        if new_username:
            if User.objects.filter(username=new_username).exists():
                messages.error(request, 'Username already exists. Please choose a different one.')
            else:
                request.session['new_username'] = new_username  # Store new username in session
                # Send email verification
                uid = urlsafe_base64_encode(force_bytes(request.user.pk))
                token = get_random_number_string(length=6)
                employee.token = token
                employee.save()

                ctx = {'token': token}
                message = render_to_string('tokenmail.html', ctx)
                send_mail(
                    'Token Verification',
                    message,
                    settings.EMAIL_HOST_USER,
                    [employee.email],
                    fail_silently=False,
                    html_message=message
                )
                messages.success(request, "We have sent a verification token to your email. Please check and fill in below form.")
                return redirect('verify_token')  # Redirect to token verification page
        else:
            messages.error(request, 'Invalid username.')

    return render(request, 'account_settings.html')  # Redirect to the profile page

@login_required
def verify_token(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        employee = Registration.objects.get(user_name=request.user.username)
        admin_token = employee.token
        if admin_token == token:
            # Token is valid, update the username
            new_username = request.session.get('new_username')
            new_password = request.session.get('new_password')
            if new_username:
                user = request.user
                user.username = new_username
                employee.user_name = new_username
                user.save()
                employee.save()

                messages.success(request, 'Username changed Successfully.')
                return redirect('user_login')
            if new_password:
                user = request.user
                user.set_password(new_password)
                employee.password = new_password
                user.save()
                employee.save()

                messages.success(request, 'Password changed Successfully.')
                return redirect('user_login')
            else:
                messages.error(request, 'No new username found. Please try again.')
        else:
            # Token is invalid, display an error message
            messages.error(request, 'Invalid token. Please try again.')

    return render(request, 'verify_token.html')

@login_required
def change_password(request):
    employee = Registration.objects.get(user_name=request.user.username)

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        if new_password:
            if User.objects.filter(password=new_password).exists():
                messages.error(request, 'Password already exists. Please choose a different one.')
            else:
                request.session['new_password'] = new_password  # Store new username in session
                # Send email verification
                uid = urlsafe_base64_encode(force_bytes(request.user.pk))
                token = get_random_number_string(length=6)
                employee.token = token
                employee.save()

                ctx = {'token': token}
                message = render_to_string('tokenmail.html', ctx)
                send_mail(
                    'Token Verification',
                    message,
                    settings.EMAIL_HOST_USER,
                    [employee.email],
                    fail_silently=False,
                    html_message=message
                )
                messages.success(request, "We have sent a verification token to your email. Please check and fill in below form.")
                return redirect('verify_token_password')  # Redirect to token verification page
        else:
            messages.error(request, 'Invalid password.')

    return render(request, 'account_settings.html')  # Redirect to the profile page

@login_required
def verify_token_password(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        employee = Registration.objects.get(user_name=request.user.username)
        admin_token = employee.token
        if admin_token == token:
            # Token is valid, update the username
            new_password = request.session.get('new_password')
            if new_password:
                user = request.user
                user.set_password(new_password)
                employee.password = new_password
                employee.confirm_password = new_password
                user.save()
                employee.save()

                messages.success(request, 'Password changed Successfully.')
                return redirect('user_login')
            else:
                messages.error(request, 'No new password found. Please try again.')
        else:
            # Token is invalid, display an error message
            messages.error(request, 'Invalid token. Please try again.')

    return render(request, 'verify_token.html')

def delete_account(request):
    user = request.user
    employee = Registration.objects.get(user_name=request.user.username)
    user.delete()
    employee.delete()
    messages.success(request,'deleted account successfully')
    return redirect('user_login')


def account_settings(request):
    return render(request, 'account_settings.html')