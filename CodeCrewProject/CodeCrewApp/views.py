from django.shortcuts import render, redirect
from .forms import contactModel, contactForm

# Create your views here.
def index(request):
    return render(request, 'CodeCrewApp/index.html')


def about(request):
    return render(request, 'CodeCrewApp/about.html')


def gallery(request):
    return render(request, 'CodeCrewApp/gallery.html')


def contact(request):
    form = contactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect("index")
    return render(request, 'CodeCrewApp/contact.html', {'form':form})


def resources(request):
    return render(request, 'CodeCrewApp/resources.html')
