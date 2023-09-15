import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from twilio.rest import Client
from .models import Address, Villager, adminAcc, Issues, WaterQuality, PumpOperator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import pywhatkit
import time

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'main.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        street = request.POST['street']
        village = request.POST['village']
        district = request.POST['district']
        add = Address.objects.create(street=street, village=village, district=district)
        add.save()
        user = User.objects.create(first_name=name, last_name="", username=phone, password="12345678")
        user = Villager.objects.create(name=name, phone=phone, address=add)
        user.save()
        return redirect('index')
    return render(request, 'register.html')


def login_user(request):
    if request.method == "POST":
        phone = request.POST['phone']
        user = User.objects.get(username=str(phone))
        login(request, user)
        return redirect('index')
    return render(request, 'login.html')

# def otp(request):
#     otp = request.POST['otp']
#     if otp == client.verify.v2.services(verify_sid) \
#         .verification_checks \
#         .create(to=verified_number, code="Please enter the OTP:"):
#         login(request, user)
#         return render(request, 'admin.html')
#     else:
#         return render(request, 'otpfilling.html')

@login_required(login_url='/login/')
def pumpOperator(request):
    user = request.user
    villager = Villager.objects.get(phone=int(user.username))
    date = datetime.date.today()
    if request.method == "POST":
        status=True
        obj = PumpOperator.objects.create(date=date, status=True, name=villager.name, village=villager.address.village, phone = villager.phone)
        obj.save()
        # villager = Villager.objects.filter(village=villager.address.village)
        # print(villager)
        # message = "Hello, This is an automatically generated message from the CFG app."

        # # Get the current time
        # now = datetime.datetime.now()

        # # Calculate the next minute
        # next_minute = (now + datetime.timedelta(minutes=1)).time()

        # # Convert the next minute to hours and minutes
        # hours = next_minute.hour
        # minutes = next_minute.minute

        # # Send the WhatsApp message
        # pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)


    return render(request, 'pumpOperator.html')

@login_required(login_url='/login/')
def adm(request):
    user = request.user
    try:
        adm = adminAcc.objects.get(phone=int(user.username))
    except:
        adm = None
    if adm is not None:
        pumpOperator = PumpOperator.objects.filter(date=datetime.date.today())
        print(datetime.date.today())
        # print(pumpOperator)
        wqc = WaterQuality.objects.filter(date=datetime.date.today())
        return render(request, 'pumptable.html', {'pumpOperator': pumpOperator,'wqc': wqc})
    else:
        return redirect('login')

def qualityMeasures(request):
    return render(request, 'water.html')

@login_required(login_url='/login/')
def issuePage(request):
    user = request.user
    villager = Villager.objects.get(phone=int(user.username))
    objs = ""
    if villager is not None:
        post = ""
        if villager.isSarpanch == True:
            post = "Sarpanch"
        elif villager.isWuc == True:
            post = "Wuc"
        else:
            post = "PumpOp"
        objs = Issues.objects.filter(stage=post, village=villager.address.village)
    else:
        objs = Issues.objects.all()
    return render(request, 'issue.html', {'objs':objs})


@login_required(login_url='/login/')
def raiseIssue(request):
    user = request.user
    print(user.username)
    villager = Villager.objects.get(phone=int(user.username))
    if request.method == 'POST':
        phone = villager.phone
        option1 = False
        option2 = False
        option3 = False
        option4 = False
        option5 = False
        
        if 'option1' in request.POST:
            checkbox_value = request.POST.get('option1')
            if checkbox_value == 'Pump not Working':
                option1 = True
            else:
                option1 = False

        if 'option2' in request.POST:
            checkbox_value = request.POST.get('option2')
            if checkbox_value == 'Water quality Issue':
                option2 = True
            else:
                option2 = False

        if 'option3' in request.POST:
            checkbox_value = request.POST.get('option3')
            if checkbox_value == 'Pipe Damage Issue':
                option3 = True
            else:
                option3 = False

        if 'option4' in request.POST:
            checkbox_value = request.POST.get('option4')
            if checkbox_value == 'Water Flow Issues':
                option4 = True
            else:
                option4 = False

        if 'option5' in request.POST:
            checkbox_value = request.POST.get('option5')
            if checkbox_value == 'Irregular water supply':
                option5 = True
            else:
                option5 = False
        
        # option1 = request.POST['option1']
        # option2 = request.POST['option2']
        # option3 = request.POST['option3']
        # option4 = request.POST['option4']
        # option5 = request.POST['option5']
        date = datetime.date.today()
        village = villager.address.village
        issue = Issues.objects.create(phone=phone, village=village, option1=option1, option2=option2, option3=option3, option4=option4, option5=option5, date=date)
        issue.save()
        return redirect('/')
    return render(request, 'raiseIssue.html')
    

@login_required(login_url='/login/')
def waterQuality(request):
    user = request.user
    print(user.username)
    villager = Villager.objects.get(phone=int(user.username))
    date = datetime.date.today()
    if request.method == 'POST':
        ph = request.POST['ph']
        taste = request.POST['taste']
        chlorine_level = request.POST['chlorine_level']
        colour = request.POST['colour']
        turbidity = request.POST['turbidity']
        water = WaterQuality.objects.create(pH=ph, taste=taste,chlorine_level=chlorine_level, colour=colour, turbidity=turbidity, date=date, name=villager.name, village=villager.address.village)
        water.save()
    return render(request, 'water.html')
        
def logout_user(request):
    logout(request)
    return redirect('/')