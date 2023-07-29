from django.shortcuts import render


def page(request):
    
    popu = "Hello page"
    return render(request, 'page.html', {"popu":popu})
