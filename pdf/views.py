from django.shortcuts import render
from .models import Profile
# Create your views here.
def index(request):
    
    context = {}
    return render(request, 'pdf/accept.html', context)