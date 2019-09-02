from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('Home/index.html')
    return HttpResponse( template.render({}, request))


def Home(request):
    context = {"message":"hola"}
  #  template = loader.get_template('/cover/index.html')
    return render(request, '/Home/index.html', context)
    #return HttpResponse(template.render(request))
