from django.shortcuts import render
from core.models import DbRouting

def index(request):
    db_list = DbRouting.objects.all()
    context = {'db_list': db_list}
    return render(request, 'core/index.html', context)
