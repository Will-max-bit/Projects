from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'roseTattoApp/index.html')

def artists_page(request):
    return render(request, 'roseTattoApp/artists_page.html')

def artist1(request):
    return render(request, 'roseTattoApp/artist1.html')
    
def artist2(request):
    return render(request, 'roseTattoApp/artist2.html')

def artist3(request):
    return render(request, 'roseTattoApp/artist3.html')

def artist4(request):
    return render(request, 'roseTattoApp/artist4.html')

def contact_us(request):
    return render(request, 'roseTattoApp/contact_us.html')