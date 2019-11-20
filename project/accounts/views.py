from django.shortcuts import render

# Create your views here.
def index(request):
    return redirect('accounts:index')
