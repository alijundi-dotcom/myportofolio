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
    )

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),

    path("musics/", show_music, name="show_music"),
    path("musics/add", create_music, name="create_music"),
    path("musics/edit/<uuid:id>", edit_music, name="edit_music"),
    path("musics/delete/<uuid:id>", delete_music, name="delete_music"),
    path("musics/json/", show_json_music, name="show_json_musico"),

    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),

]