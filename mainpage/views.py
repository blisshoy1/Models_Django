from django.shortcuts import render

# Create your views here.
from .models import Info


def index(request):
    info = Info.objects.all()
    return render(request, 'mainpage/index.html', {'info': info})
