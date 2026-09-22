import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, logout 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from main.models import Experience, Project, Musics
from main.forms import ProjectForm, MusicForm

# Create your views here.

##TUTORIAL 3 START ###
def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Ali",
        "form": form,
    }
    return render(request, "projects_form.html", context)
##TUTORIAL 3 END ###

### TUGAS 3

## fitur tambah musik
def create_music(request):
    form = MusicForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Musik Anda berhasil ditambahkan!")
        return redirect("main:show_music")

    context = {
            "name": "Ali",
            "form": form,
        }
    
    return render(request, "musics_form.html", context)

# fitur edit musik 
def edit_music(request, id):
    music = get_object_or_404(Musics, pk=id)
    form = MusicForm(request.POST or None, instance=music)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_music")
    
    context = {
                "name": "Ali",
                "form": form,
            }
        
    return render(request, "edit_music.html", context)

#fitur hapus musik -- delete
def delete_music(request, id):
    music = get_object_or_404(Musics, pk=id)
    music.delete()
    return redirect("main:show_music")

def show_json_music(request):
    data = Musics.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

### END TUGAS 3
def show_main(request):
    #baca cookie last login
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Ali Jundi Qowi",
        "npm": "2506611585",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
            "Mahasiswa yang juga tertarik gaya gravitasi bumi"
        ),
        "last_login": last_login, 
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

#fungsi show_projects diubah sesuai tutor 3
def show_projects(request):

    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    context= {
        "name": "Ali",
        "project_list": Project.objects.all(),
        "title_query": title_query,
    }   
    return render(request, "projects.html", context)

#tambahan fungsi dari tutor 3
def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")
#end tambahan tutor 3

# Tutorial 4 
# tambah fungsi register
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Ali", #nama diubah ke nama sendiri
        "form": form,
    }
    return render(request, "register.html", context)

# buat view login dan form sign in 
def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user();
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response
    context = {
        "name": "Ali", #ubah nama pemilik
        "form": form,
    }
    return render(request, "login.html", context)

# logout
def logout_user(request):
    logout(request)
    respone = redirect("main:show_main")
    respone.delete_cookie('last_login')
    return respone
    # fungsi diubah untuk menghapus cookie saat logout

# End Tutorial 4