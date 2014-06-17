from django.http import (HttpResponseRedirect,
                         HttpResponse)
from django.shortcuts import (render_to_response,
                              render)
from django.template import RequestContext

# View for index page
def home(request):
    context = RequestContext(request)
    return render(request,'index.html',context)
