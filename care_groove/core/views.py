from django.http import (HttpResponseRedirect,
                         HttpResponse)
from django.shortcuts import (render_to_response,
                              render)
from django.template import RequestContext

# View for index page
def home(request):
    context = RequestContext(request)
    return render_to_response('index.html',{}, context)
    #return render(request, 'index.html', {'user': request.user})
