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
from django.urls import reverse_lazy


# Create your views here.
def customer_reg(request):
    
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        m_name = request.POST.get('m_name')
        l_name = request.POST.get('l_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        aadhar = request.FILES.get('aadhar')
        profile_photo = request.FILES.get('profile_photo')

        c_name = request.POST.get('c_name')
        c_register_no = request.POST.get('c_register_no')
        c_email = request.POST.get('c_email')
        c_mobile = request.POST.get('c_mobile')
        c_address = request.POST.get('c_address')
        c_incorporation = request.FILES.get('c_incorporation')
        p_card = request.FILES.get('p_card')

        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        image_data = request.POST.get('image_data')

        # Generate a 4-digit UUID
        unique_id = str(uuid.uuid4())[:4]

        if image_data is not None:
            try:
                # Decode base64 data
                image_data = image_data.split('base64,')[1]
                image = Image.open(BytesIO(base64.b64decode(image_data)))

                # Save image to MEDIA_ROOT directory
                image_path = os.path.join(settings.MEDIA_ROOT, 'photos', 'temp.jpg')
                image.save(image_path, format='JPEG')

                # Sending email
                ctx = {
                    'f_name': f_name,
                    'l_name': l_name,
                }
                message = render_to_string('welcome_mail.html', ctx)

                send_mail(
                    'User Info',
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                    html_message=message
                )

                send_mail(
                    'User Info',
                    message,
                    settings.EMAIL_HOST_USER,
                    ['salonipatil0777@gmail.com'],
                    fail_silently=False,
                    html_message=message
                )

                # Save the user login information if passwords match
                customer_reg = Customer_Reg.objects.create(f_name=f_name, m_name=m_name, l_name=l_name, mobile=mobile,email=email, aadhar=aadhar, profile_photo=profile_photo, c_name=c_name, c_register_no=c_register_no, c_email=c_email, c_mobile=c_mobile, c_address=c_address, c_incorporation=c_incorporation,p_card=p_card,
                name=name,date=date,time=time,location=location,photo='photos/temp.jpg', unique_id=unique_id)

                customer_reg.save()

                return redirect('home')  # Redirect to home page after successful registration

            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
        else:
            return JsonResponse({'success': False, 'error': 'Image data is missing.'})

    return render(request, 'customer_reg.html')



def manage_customer(request):
    customer = Customer_Reg.objects.all()

    context ={
        'manage_customer':customer
    }

    return render(request, 'manage_customer.html', context)



def customer_home(request):
    return render(request, 'customer_home.html')



def customer_menu_card(request):
    customer = Customer_Reg.objects.all()

    context ={
        'manage_customer':customer
    }
    return render(request, 'customer_menu_card.html',context)



def customer_help(request):
    if request.method == 'POST':
        your_name = request.POST.get('your_name')
        your_email =request.POST.get('your_email')
        company_name_help =request.POST.get('company_name_help')
        subject_help =request.POST.get('subject_help')
        select_department =request.POST.get('select_department')
        your_massage =request.POST.get('your_massage')

        customer_help =CustomerHelp.objects.create(your_name=your_name, your_email=your_email, company_name_help=company_name_help, subject_help=subject_help, select_department=select_department,  your_massage=your_massage)

        customer_help.save()

        return redirect('customer_home')

    return render(request, 'customer_help.html')


def delete_customer(request,id):
    delete_customer=Customer_Reg.objects.get(id=id)
    delete_customer.delete()

    return redirect('manage_customer')


def customer_user_login(request):
    if request.method == 'POST':
        user_name1 = request.POST.get('user_name1')
        password1 = request.POST.get('password1')

        # Authenticate user
        user = authenticate(username=user_name1, password=password1)

        if user is not None:
            # If user is authenticated, log them in
            login(request, user)
            return redirect('customer_menu_card')
        else:
            # If authentication fails, you might want to handle the error here
            # For example, render the login form again with an error message
            return render(request, 'customer_user_login.html', {'error': 'Invalid username or password'})
        

    return render(request, 'customer_user_login.html')


def logout_view2(request):
    logout(request)
    return redirect(reverse_lazy('customer_home'))


def customer_view_profile(request):
    username=request.user.username
    profile = Customer_Reg.objects.filter(user_name=username)
    context = {
        'profiles': profile
    }
    return render(request, 'view_profile.html', context)


def customerleadpanel_tab(request):
    customer = Customer_Reg.objects.all()

    context ={
        'manage_customer':customer
    }
    return render(request, 'customerleadpanel_tab.html',context)
