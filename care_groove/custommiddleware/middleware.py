from django.http import (HttpResponseRedirect,
                         HttpResponse,
                         Http404)
from core import models as core_models
from django.conf import settings
print core_models.host_details.objects.get(pk=1)


class host_middleware(object):
    def process_request(self, request):
        comment = get_object_or_404(core_models.host_details, pk=2)
        print comment
        print core_models.host_details.objects.get(pk=3)
        print core_models.host_details.objects.filter(host_name = request.META['HTTP_HOST']).exists()
        if core_models.host_details.objects.filter(host_name = request.META['HTTP_HOST']).exists():
            raise Http404
            return None
