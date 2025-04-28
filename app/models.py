from django.db import models

# Create your models here.


class Registration(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    middle_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=15,null=True)
    address = models.TextField(null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to='images/',null=True)
    
    company_name = models.CharField(max_length=100,null=True)
    company_register_no = models.CharField(max_length=100,null=True)
    company_email = models.EmailField(null=True)
    company_mobile = models.CharField(max_length=15,null=True)
    company_address = models.TextField(null=True)
    company_incorporation = models.ImageField(upload_to='images/',null=True)
    pan_card = models.ImageField(upload_to='images/',null=True)
    
    user_name = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    confirm_password = models.CharField(max_length=100,null=True)

    token = models.CharField(max_length=6,null=True)

    def __str__(self):
        return self.user_name


class AgentReg(models.Model):
    first_name1 = models.CharField (max_length=100, null=True)
    middle_name2 = models.CharField (max_length=100, null=True)
    last_name3 = models.CharField (max_length=100, null=True)
    mobile1 = models.CharField (max_length=100, null=True)
    email1 = models.EmailField (max_length=100, null=True)
    aadhar1 = models.FileField (upload_to='pics/', null=True)
    photo1 = models.FileField (upload_to='pics/', null=True)
    unique_id = models.CharField(max_length=4 ,null=True)



class HelpHire(models.Model):
    help_name=models.CharField(max_length=100,null=True)
    help_email=models.CharField(max_length=100,null=True)
    help_company_name_help=models.CharField(max_length=100,null=True)
    subject_help2=models.CharField(max_length=100,null=True)
    select_department_help=models.CharField(max_length=100,null=True)
    your_massage_help=models.CharField(max_length=100,null=True)