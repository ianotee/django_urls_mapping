from django.shortcuts import render


def about(request):
    about = "Hello the about page"
    return render(request, "about.html", {"about": about})
