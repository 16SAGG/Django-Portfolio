from django.shortcuts import render
from .models import projects

def home(request):
    myProjects = projects.objects.all()
    ctxt = {
        'myProjects': myProjects,
    }
    return render(request, 'home.html', ctxt)
