from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy
from .models import Contact
from django.contrib.auth.decorators import login_required
import os
from django.shortcuts import redirect
import datetime



class ContactFormView(CreateView):
    template_name = 'QRer/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('QRer:contact_result')
    model = Contact

class ContactResultView(TemplateView):
    template_name = "QRer/contact_result.html"


# Create your views here.

sigma = {'0':'92','1':'38','2':'47','3':'05','4':'58','5':'09','6':'89','7':'96','8':'30','9':'12'}
def encryption(m):
    c = [sigma[a] for a in m]
    return c
 

#def rend(request):
    #return render(request, "QRer/result.html")    

def frontpage(request):
    return render(request, "QRer/top.html")


def resultpage(request):
    return render(request, "QRer/result.html")


def index2(request):
    return render(request, "QRer/index.html")

def logout_view(request):
    return render(request, "QRer/logged_out.html")


 
def sample(request):
    dt_now = datetime.datetime.now()
    time_left = dt_now + datetime.timedelta(minutes=90)
    strftime_time_left = time_left.time_left_at.strftime('%B %d,%Y %H:%M:%S')
    context = {
    'time_left': strftime_time_left
    }
    return render(request, 'QRer/main.html', context)    



@login_required(login_url='/QRer/accounts/login')
def maker(request):
    if not request.user.is_superuser:
        return redirect('QRer:index')
    p1 = request.POST.get('p1', '')
    alert = {'error':"正しく入力してください"}
    try:
        poke = ''.join(encryption(p1))
    except:
        return render(request, 'QRer/index.html', alert)

    params = {'p2': f"https://chart.apis.google.com/chart?cht=qr&chs=300x300&chl={poke}", 'p3':f"学籍番号：{p1}"}
    alert = {'error':"*学籍番号を数字8桁で正しく入力してください"}
    try:
        if 20220300 > int(p1) > 20170000:
            return render(request, 'QRer/index.html', params)
        else:
            return render(request, 'QRer/index.html', alert)
    except:
        return render(request, 'QRer/index.html')


@login_required(login_url='/QRer/accounts/login')
def index(request):
    username = request.user
    alert = {'error':"生徒用アカウントでログインして下さい"}
    params = {'p2':"", 'p3':""}
    dt_now = datetime.datetime.now()
    time_left = dt_now + datetime.timedelta(minutes=1)
    strftime_time_left = time_left.strftime('%B %d,%Y %H:%M:%S')
    #context = {'time_left': strftime_time_left}

    try:
        poke = ''.join(encryption(str(username)))
    except:
        return render(request, 'QRer/main.html', alert)
    if request.method == "POST":
            if "type_1" in request.POST:
                params = {'url':f"https://chart.apis.google.com/chart?cht=qr&chs=300x300&chl={poke}", 'p3':f"学籍番号：{username}", 'p4':'通常用 /', 'p5':'/static/js/sample.js'}
                print(strftime_time_left)
            elif "type_2"  in request.POST:
                params = {'url':f"https://chart.apis.google.com/chart?cht=qr&chs=300x300&chl={username}", 'p3':f"学籍番号：{username}", 'p4':'例外用 /', 'p5':'/static/js/sample.js'}

    
    return render(request, 'QRer/main.html', params)
