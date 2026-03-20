from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Привет! Это главная страница Dacha Finder</h1>")
