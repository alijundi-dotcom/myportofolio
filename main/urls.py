from django.urls import path

from main.views import (
    show_main, 
    show_experience, 
    show_music,
    create_music,
    edit_music,
    delete_music,
    show_json_music,
    show_projects,
    create_project,
    get_projects_json,
    delete_project,
    register,
    login_user,
    logout_user,
    toggle_star,
    )

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("musics/", show_music, name="show_music"),
    #Tugas 3
    path("musics/add", create_music, name="create_music"),
    path("musics/edit/<uuid:id>", edit_music, name="edit_music"),
    path("musics/delete/<uuid:id>", delete_music, name="delete_music"),
    path("musics/json/", show_json_music, name="show_json_musico"),
    # END Tugas 3
    # Tutorial 3
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    # END Tutorial 3
    # Tutorial 4
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/",toggle_star,name="toggle_star",),

    # END Tutorial 4
]