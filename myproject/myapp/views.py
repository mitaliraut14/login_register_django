from django.shortcuts import render,redirect
from myapp.models import User
import datetime
# Create your views here.

def register(request):
    if request.method=="POST":
        name=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        dob=request.POST['dob']
        phn=request.POST['phn']
        add=request.POST['add']
        upass=request.POST['pass']
        cupass=request.POST['cpass']
        error={}
        err=0
        success={}
        #blank field validation start
        if name=="":
            err=1
            error['errnamemsg']="Name field cannot be Blank"
        elif email=="":
            err=1
            error['erremailmsg']="Username field cannot be Blank"
        elif dob=="":
            err=1
            error['errdobmsg']="DOB field cannot be Blank"
        elif phn=="":
            err=1
            error['errphnmsg']="Phn no field cannot be Blank"
        elif add=="":
            err=1
            error['erraddmsg']="Address field cannot be Blank"
        elif upass=="":
            err=1
            error['errpassmsg']="Password field cannot be Blank"
        elif cupass=="":
            err=1
            error['errcupassmsg']="Confirm Password field cannot be Blank"
        elif upass != cupass:
            err=1
            error['errmismatch']="Password and confirm password didn't matched"
        #field validation end

        if err==0:
            # u=User(username=email,password=upass,first_name=name,is_active=1)
            u=User.objects.create(username=email,password=upass,firstname=name,lastname=lname,DOB=dob,address=add,phone_no=phn,created_on=datetime.datetime.now())
            print(u)
            u.save()
            success['msg']="User Created Successfully!"
            return render(request,'register.html',success)
          
        else:
            return render(request,'register.html',error)
    
    else:
            return render(request,'register.html')
    
def login(request):
    if request.method=="POST":
        
        email=request.POST['email']
        upass=request.POST['upass']
        usuccess={}
        user =User.objects.filter(username=email)
        
        if user is not None:
            
            if email==email and upass==upass:
                return redirect('/udash')
            else:
                usuccess['umsg']="username or password is worng!"
                return render(request,'login.html',usuccess)    
        else:
            usuccess['umsg']="User Not Registered!"
            return render(request,'login.html',usuccess)    

    else:



        return render(request,'login.html')
    
def dashboard(request):
    p=User.objects.all()
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

def index(request):
    return render(request,'index.html') 