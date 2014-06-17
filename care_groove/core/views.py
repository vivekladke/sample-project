from django.http import (HttpResponseRedirect,
                         HttpResponse)
from django.shortcuts import (render_to_response,
                              render)


# View for index page
def home(request):
    print request.user
    return render_to_response('index.html', {'user': request.user})
