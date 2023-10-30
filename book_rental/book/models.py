from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10,null=True)
    dob = models.DateField()
    address = models.CharField(max_length=50,null=True)
    def _str_(self):
        return self.user.username

class Book(models.Model):
    book_name = models.CharField(max_length=20, null=True)
    price1 = models.CharField(max_length=30, null=True)
    price2 = models.CharField(max_length=30, null=True)
    type = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)

class Feedback(models.Model):
    feedback_name = models.CharField(max_length=20,null=True)
    feedback_contact = models.CharField(max_length=30, null=True)
    feedback_email = models.CharField(max_length=10,null=True)
    feedback_comment = models.CharField(max_length=15,null=True)

class Booked(models.Model):
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30,null=True)
    mobile = models.CharField(max_length=30,null=True)
    book_name = models.CharField(max_length=30,null=True)
    booking_date = models.CharField(max_length=20,null=True)
    days = models.CharField(max_length=10,null=True)
    price1 = models.CharField(max_length=20,null=True)
    price2 = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=20,null=True)

class Contact(models.Model):
    con_name = models.CharField(max_length=20,null=True)
    con_mobile = models.CharField(max_length=30, null=True)
    con_email = models.CharField(max_length=10,null=True)
    con_purpose = models.CharField(max_length=15,null=True)
