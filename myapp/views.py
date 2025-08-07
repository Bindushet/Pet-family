from django.shortcuts import render
# import requests
from myapp.models import UserRegistration,UserLogin,Adoptiondata
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        fullname = request.POST.get('t1')
        contact = request.POST.get('t3')
        email = request.POST.get('t2')
        password = request.POST.get('t4')
        ucount = UserRegistration.objects.filter(email=email).count()
        if ucount >= 1:
            return render(request, 'signup.html', {'msg': 'this user is already exist'})
        else:
            UserRegistration.objects.create(fullname=fullname,contact=contact,email=email, password=password)
            UserLogin.objects.create(username=email, password=password, utype='user')
            return render(request, 'signup.html', {'msg': 'Thank you for registration..!go to home to login'})
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('pswd')
        request.session['username'] = username
        ucount = UserLogin.objects.filter(username=username).count()
        if ucount >= 1:
            udata = UserLogin.objects.get(username=username)
            uname=username
            upass = udata.password
            if upass == password:
                if uname == "admin@gmail.com":
                    return render(request, 'admin_home.html')
                else :
                    return render(request, 'user_home.html')
            else:
                return render(request, 'index.html', {'msg': 'invalid password'})
        else:
            return render(request, 'index.html', {'msg': 'invalid username'})
    return render(request, 'index.html')

def adopt(request):
    if request.method == "POST":
        fullname= request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        address= request.POST.get("address")
        type = request.POST.get("type")
        reason = request.POST.get("reason")
        Adoptiondata.objects.create(fullname=fullname,email=email,contact=contact,address=address,type=type,reason=reason)

    # Send email to the user
    
        subject = "Adoption Application Received"
        message = (
            f"Dear {fullname},\n\n"
            "Thank you for submitting your adoption application to Pet Family.\n"
            "Here are the details you provided:\n"
            f"- Full Name: {fullname}\n"
            f"- Email: {email}\n"
            f"- Contact: {contact}\n"
            f"- Address: {address}\n"
            f"- Type of Pet: {type}\n"
            f"- Reason for Adoption: {reason}\n\n"
            "Our team will review your application and get back to you shortly.\n\n"
            "Best regards,\n"
            "Pet Family Team"
        )
        
        # email_msg = 
        send_mail(subject, message,'bsshet04@gmail.com', [email])
        # email_msg.send()

        return render(request, 'adopt.html',{'msg':'Thank you for your application. We have sent you an email confirmation!'})
    return render(request,'adopt.html')

def food(request):
    return render(request,'food.html')

def shop(request):
    return render(request,'shop.html')

def about(request):
    return render(request,'index.html')

# def admin_home(request):
#     adata = Adoptiondata.objects.all()
#     return render(request,'admin_home.html',{'adata':adata})

def admin_home(request):
    adata=Adoptiondata.objects.all()
    print(adata)
    return render(request,'admin_home.html',{'adata':adata})

# def admin_home(request):
#         test_data = [
#         {"fullname": "John Doe", "email": "john@example.com", "contact": "1234567890", "address": "123 St", "type": "Dog", "reason": "Companionship"},
#     ]
#         return render(request,'admin_home.html',{'adata': test_data})


def user_home(request):
    # J_data=request.session['username']
    return render(request,'user_home.html')