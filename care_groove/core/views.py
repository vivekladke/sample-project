from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('base.html')
