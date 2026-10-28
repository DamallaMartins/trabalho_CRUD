from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Geeks! Welcome to your first Django app.")