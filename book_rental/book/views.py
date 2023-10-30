from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *
import datetime

def index(request):
    return render(request,'index.html')

def signup(request):
    error = ""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        p = request.POST['pwd']
        gen = request.POST['gender']
        pic = request.POST['profile_pic']
        addr=request.POST['address']
        d=request.POST['dob']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Signup.objects.create(user=user,mobile=con,image=pic,gender=gen,address=addr,dob=d)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signup.html',d)

def login(request):
    error=""
    if request.method == "POST":
        ur = request.POST['uname']
        pd = request.POST['pwd']
        user = auth.authenticate(username=ur,password=pd)
        try:
            if user.is_staff:
                auth.login(request,user)
                error = "no"
            elif user is not None:
                auth.login(request,user)
                return redirect('user_home')
                error = "not"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'login.html',d)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'admin_home.html')


def Logout(request):
    logout(request)
    return redirect('index')

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    user2 = Signup.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']
        gen = request.POST['gender']
        add = request.POST['address']
        user2.user.first_name = f
        user2.user.last_name = l
        user2.mobile = con
        user2.gender = gen
        user2.address = add

        try:
            user2.save()
            user2.user.save()
            error = "no"
        except:
            error = "yes"
        try:
            i = request.FILES['image']
            user2.image = i
            user2.save()
            error = "no"
        except:
            pass
    d = {'user2': user2, 'error': error}
    return render(request,'user_home.html',d)

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Signup.objects.all()
    d = {'data':data}
    return render(request,'view_users.html',d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_users')

def add_book(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=='POST':
        n = request.POST['book']
        p1 = request.POST['price1']
        p2 = request.POST['price2']
        s = request.POST['status']
        i = request.FILES['image']
        try:
            Book.objects.create(book_name=n,price1=p1,price2=p2,type='hello',status=s,image=i)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_book.html',d)

def view_book_admin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Book.objects.all()
    d = {'data':data}
    return render(request,'view_book_admin.html',d)

def delete_book(request,id):
    emp=Book.objects.get(id=id)
    emp.delete()
    return redirect('view_book_admin')

def edit_book(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Book.objects.get(id=pid)
    error=""
    if request.method=='POST':
        n = request.POST['book']
        p2 = request.POST['price2']
        p1 = request.POST['price1']
        s = request.POST['status']
        data.book_name = n
        data.price1 = p1
        data.price2 = p2
        data.status = s
        try:
            data.save()
            error="no"
        except:
            error="yes"
    d = {'data':data,'error':error}
    return render(request,'edit_book.html',d)

def change_bookimage(request,id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    data = Book.objects.get(id=id)
    if request.method == 'POST':
        l = request.FILES['image']
        data.image = l
        try:
            data.save()
            error="no"
        except:
            error="yes"
    d = {'error': error,'data':data}
    return render(request,'change_bookimage.html',d)

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passwordadmin.html',d)

def view_feedback(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Feedback.objects.all()
    data2 = Contact.objects.all()
    d = {'data':data,'data2':data2}
    return render(request,'view_feedback.html',d)

def feedback(request):
    if not request.user.is_authenticated:
        return redirect('feedback')
    error=""
    if request.method=='POST':
        n = request.POST['fname']
        p = request.POST['fphone']
        e = request.POST['femail']
        c = request.POST['fcomment']
        try:
            Feedback.objects.create(feedback_name=n,feedback_contact=p,feedback_email=e,feedback_comment=c)
            error = "no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'feedback.html',d)

def delete_feedback(request,id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    feedback = Feedback.objects.get(id=id)
    feedback.delete()
    return redirect('view_feedback')

def view_book_user(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Book.objects.all()
    d = {'data':data}
    return render(request,'view_book_user.html',d)

def buy_now(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Book.objects.get(id=pid)
    dd=datetime.datetime.now()
    error=""
    if request.method=='POST':
        f=request.POST['fname']
        k=request.POST['lname']
        e=request.POST['email']
        c=request.POST['contact']
        bn=request.POST['book']
        p=request.POST['price']
        d=request.POST['date']
        a=request.POST['address']
        try:
            Booked.objects.create(first_name=f,last_name=k,email=e, mobile=c,book_name=bn,price1=p,booking_date=d,address=a,status="Buy Pending")
            error = "no"
        except:
            error = "yes"
    d = {'data':data,'dd':dd,'error':error}
    return render(request,'buy_now.html',d)

def rent_book(request,id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Book.objects.get(id=id)
    dd = datetime.datetime.now()
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        k = request.POST['lname']
        e = request.POST['email']
        c = request.POST['contact']
        bn = request.POST['book']
        p = request.POST['price']
        d = request.POST['date']
        dy = request.POST['day']
        a = request.POST['address']
        pr = int(p) * int(dy)
        try:
            Booked.objects.create(first_name=f, last_name=k, email=e, mobile=c, book_name=bn, price1=pr, booking_date=d,days=dy,
                                  address=a, status="Rent Pending")
            error = "no"
        except:
            error = "yes"
    d = {'data': data, 'dd': dd, 'error': error}
    return render(request, 'rent_book.html', d)

def view_booking(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Booked.objects.all()
    d = {'data': data}
    return render(request,'view_booking.html',d)

def cancel_booking(request,id):
    booking=Booked.objects.get(id=id)
    booking.delete()
    return redirect('view_booking')

def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passworduser.html',d)

def contact(request):
    error=""
    if request.method=='POST':
        n = request.POST['cname']
        pn = request.POST['cphone']
        e = request.POST['cemail']
        p = request.POST['cpurpose']
        try:
            Contact.objects.create(con_name=n,con_mobile=pn,con_email=e,con_purpose=p)
            error = "no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'contact.html')

def delete_contact(request,id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('view_feedback')

def view_booking_admin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Booked.objects.all()
    d = {'data': data}
    return render(request,'view_booking_admin.html',d)

def delete_booking(request,id):
    booking=Booked.objects.get(id=id)
    booking.delete()
    return redirect('view_booking')

def change_status(request,id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking=Booked.objects.get(id=id)
    error=""
    if request.method == "POST":
        rs = request.POST['rstatus']
        booking.status = rs
        try:
            booking.save()
            error = "no"
        except:
            error = "yes"
    d = {'booking': booking,'error':error}
    return render(request,'change_status.html',d)

def search(request):
    n=request.POST['name']
    data=Book.objects.filter(book_name__icontains=n)
    data2="Sorry No Book Found"
    if data:
        d={'data':data}
    else:
        d = {'data2': data2}
    return render(request,'view_book_user.html',d)
