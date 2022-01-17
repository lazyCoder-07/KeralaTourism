from django.contrib import messages
from django.shortcuts import render
from kt.models import ktd, chatinput


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def Register(request):
    return render(request, 'Register.html')

def home2(request):
    return render(request, 'home2.html')

def login(request):
    return render(request, 'login.html')

def gallery(request):
    return render(request, 'gallery.html')

def athirappilly(request):
    return render(request, 'athirappilly.html')

def kovalam(request):
    return render(request, 'kovalam.html')

def nelliyampathy(request):
    return render(request, 'nelliyampathy.html')

def save(request):
    member = ktd(name=request.POST['name'],psw1=request.POST['psw1'],psw2=request.POST['psw2'], Email=request.POST['Email'])
    member.save()
    return render(request,'home2.html',{'member': member})


def save1(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        psw1 = request.POST.get("psw1")
        psw2 = request.POST.get("psw2")
        Email = request.POST.get("Email")
        try:
            member1 =ktd(name=name, psw1=psw1, psw2=psw2, Email=Email)
            member1.save()
            return render(request,'login.html', {'member': member1, 'member1': member1})
        except:
            return render(request,'home.html', {'member': member1})

def save2(request):
    if request.method == 'POST':
        message = request.POST.get("message")
        try:
            member1 =chatinput(message=message)
            member1.save()
            return render(request,'home2.html')
        except:
            return render(request,'login.html')



def loginpage(request):
    if request.method == "POST":
        try:
            userdetails = ktd.objects.get(name=request.POST['name'], psw1=request.POST['psw1'])
            print("username=", userdetails)
            request.session['name']=userdetails.name
            return render(request, 'home2.html')
        except ktd.DoesNotExist as e:
            messages.success(request,'Username / Password Invalid...!')
    return render(request, 'login.html')



