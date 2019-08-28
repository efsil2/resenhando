from django.shortcuts import render

def films_list(request):
    return render(request, 'controller/films_list.html',{})


