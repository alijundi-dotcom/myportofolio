from django.shortcuts import render


def landing_page(request):
    return render(request, "index.html")
def burhan_page(request):
    return render(request, "burhan.html")
def skills_page(request):
    return render(request, "skills.html")
def exp_page(request):
    return render(request, "exp.html")