from django.http import (HttpResponseRedirect,
                         HttpResponse,
                         Http404)
import core.models as core_models
from django.conf import settings


class host_middleware(object):
    def process_request(self, request):
        #if core_models.host_info.objects.filter(host_name = request.META['HTTP_HOST']).exists():
        if request.META['HTTP_HOST'] != '127.0.0.1:8000':
            raise Http404
            return None
        #else:
