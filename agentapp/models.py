from django.db import models

# Create your models here.

class Customer_Reg(models.Model):
    f_name = models.CharField (max_length=100, null=True)
    m_name = models.CharField (max_length=100, null=True)
    l_name = models.CharField (max_length=100, null=True)
    mobile = models.CharField (max_length=100, null=True)
    email = models.EmailField (max_length=100, null=True)
    aadhar = models.FileField (upload_to='pics/', null=True)
    profile_photo = models.FileField (upload_to='pics/', null=True)
    
    c_name=models.CharField(max_length=100,null=True)    
    c_register_no=models.CharField(max_length=100,null=True)          
    c_email=models.CharField(max_length=100,null=True)
    c_mobile=models.CharField(max_length=100,null=True)     
    c_address=models.CharField(max_length=100,null=True)    
    c_incorporation=models.ImageField(upload_to='pics/',null=True)
    p_card=models.ImageField(upload_to='pics/',null=True)
    
    name = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='photos/',null=True)
    date = models.CharField(max_length=100, null=True)
    time = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=255, null=True)
    unique_id = models.CharField(max_length=4 ,null=True)

    
class CustomerHelp(models.Model):
    your_name=models.CharField(max_length=100,null=True)
    your_email=models.CharField(max_length=100,null=True)
    company_name_help=models.CharField(max_length=100,null=True)
    subject_help=models.CharField(max_length=100,null=True)
    select_department=models.CharField(max_length=100,null=True)
    your_massage=models.CharField(max_length=100,null=True)