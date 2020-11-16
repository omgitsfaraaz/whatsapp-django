from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'whatsapp_app/home.html')

def SendData(request):
    if request.method == 'POST':
        Ph = request.POST['Phone']
        Message = request.POST['Message']
        print(Ph, Message)
        msg = 'Message was successfully sent...'
        return render(request, "whatsapp_app/home.html", {'msg': msg})
    else:
        return HttpResponse("<h1>Your message was not delivered.</h1>")