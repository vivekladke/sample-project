from django.http import Http404
from core import models as core_models
from django.conf import settings


class host_middleware(object):
    def process_request(self, request):
        if not core_models.HostDetails.objects.filter(
                host_name = request.get_host().split(":")[0]).exists():
            raise Http404
        else:
            host = core_models.HostDetails.objects.filter(
                host_name = request.get_host().split(":")[0])
            settings.DATABASES['user']['NAME'] = host[0].database_name
            settings.DATABASES['user']['USER'] = host[0].user_name
            settings.DATABASES['user']['PASSWORD'] = host[0].password
            settings.DATABASES['user']['HOST'] = host[0].host_name
            settings.DATABASES['user']['PORT'] = host[0].port
            print "Id"
            print host[0].id
            request.served_by_id = host[0].id
            print request.served_by_id
        return None
