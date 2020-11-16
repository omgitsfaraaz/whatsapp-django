from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'whatsapp_app/home.html')

def whatsApp(Ph, Message):
    import time
    import webbrowser as web
    import pyautogui as pg
    Phone = "+91"+Ph
    web.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Message)
    time.sleep(9)
    pg.press('enter')

def SendData(request):
    if request.method == 'POST':
        Ph = request.POST['Phone']
        Message = request.POST['Message']
        #print(Ph, Message)
        whatsApp(Ph, Message)
        msg = 'Your message was sent successfully!'
        return render(request, "whatsapp_app/home.html", {'msg': msg})
    else:
        return HttpResponse("<h1>Your message was not delivered.</h1>")