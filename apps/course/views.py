from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
	context = {
		"courses":Course.objects.all()
	}
	return render(request, "course/index.html", context)

def create(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect('/')

def destroy(request, id):
	context = {
		"courses" : Course.objects.get(id=id)
	}
	return render(request, "course/remove.html", context)

def confirm(request, id):
	courses=Course.objects.get(id=id).delete()
	return redirect('/')
