from django.shortcuts import render

def home(request):
    return render(request, 'whatsapp_app/home.html')