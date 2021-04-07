from django.shortcuts import render


def myapp_index(request):
    return render(request, "myapp_index.html")


