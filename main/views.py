from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse

from main.models import Experience
from main.models import Musics
from main.models import Project

# Create your views here.

##TUTORIAL 3 START ###
def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "projects_form.html", context)
##TUTORIAL 3 END ###

def show_main(request):
    context = {
        "name": "Ali Jundi Qowi",
        "npm": "2506611585",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
            "Mahasiswa yang juga tertarik gaya gravitasi bumi"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Ali",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_music(request):
    context = {
        "name": "Ali",
        "music_list": Musics.objects.all(),

    }
    return render(request, "musics.html", context)

def show_projects(request):
    context= {
        "name": "Ali",
        "project_list": Project.objects.all(),
    }   
    return render(request, "projects.html", context)
