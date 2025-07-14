from django.shortcuts import render

# Create your views here.
def registrationpage(request):
    return render(request, 'registration.html')

def test(request):
    return render(request, 'test.html')

def requestpage(request):
    return render(request, 'request.html')