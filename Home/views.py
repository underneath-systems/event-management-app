from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic


# def index(request):
#     template = loader.get_template('Home/index.html')
#     return HttpResponse( template.render({}, request))


class Index(View):
    template = 'Home/index.html'
    # template = loader.get_template('Home/index.html')
    context = {'title': 'Index'}

    def get(self, request):
        """
            Get in my Home.
        """
        return render(request, self.template, self.context)

