from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic


class Create(View):
    template = 'event/create.html'
    # template = loader.get_template('Home/index.html')
    context = {'title': 'create event'}

    def get(self, request):
        """
            Get in my Home.
        """
        return render(request, self.template, self.context)
