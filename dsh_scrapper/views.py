from django.http import HttpResponse

from .models import Client

def index(request):
    www_list = Client.objects.all()
    return HttpResponse(www_list)


