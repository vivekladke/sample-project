from django.http import (HttpResponseRedirect,
                         HttpResponse,
                         Http404)
from core import models as core_models
from django.conf import settings


class host_middleware(object):
    def process_request(self, request):
        if not core_models.host_details.objects.filter(
                host_name = request.get_host().split(":")[0]).exists():
            raise Http404
            return None
        else:
            host = core_models.host_details.objects.filter(
                host_name = request.get_host().split(":")[0])
            settings.DATABASES['users']['NAME'] = host
