from django.shortcuts import render


def home(request):

    greetings ="Hello Ian You are a software Engineer"
    return render(request, "home.html", {"greetings":greetings})
    
