from django.http import HttpResponse

# Create your views here.
def index(): 
    output = "test"
    return HttpResponse(output)