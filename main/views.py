from django.shortcuts import render

from main.models import Experience
from main.models import Musics

# Create your views here.

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