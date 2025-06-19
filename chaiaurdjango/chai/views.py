from django.shortcuts import render

# Create your views here.
def all_chai(request):
    return(request, 'chai/all_chai.html')