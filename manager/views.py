from django.shortcuts import render

# Create your views here.

def RecordsPage(request):
    
    return render(request,'records.html')