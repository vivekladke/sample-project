from django.http import (HttpResponseRedirect,
                         HttpResponse)
from django.shortcuts import (render_to_response,
                              render)


# View for index page
def home(request):
    return HttpResponse("Core-groove says hello world!")
