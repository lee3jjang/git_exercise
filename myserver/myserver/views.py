from django.http import HttpResponse

def index(request):
    a = 4
    b = 3
    return HttpResponse(f"{a} + {b} = {a+b}")