from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):

    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text': 'Posted!!'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'Get!!'})