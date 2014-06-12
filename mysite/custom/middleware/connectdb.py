from core.models import DbRouting
from django.conf import settings


class RequestDB(object):
    def process_request(self,request):
        print "Host"
        host_str = request.get_host()
        host_str = host_str.split(':')
        print host_str[0]
        try:
            host_list = DbRouting.objects.get(host_name=host_str[0])
        except Exception:
            host_list = None
        
        if host_list :
            print "DataBase Name :" + host_list.db_name
            print "User Name :" + host_list.user_name
            print "Password Name :" + host_list.password
            print "Port :" + host_list.port
            settings.DATABASES['users']['NAME']= host_list.db_name
            settings.DATABASES['users']['USER']= host_list.user_name
            settings.DATABASES['users']['PASSWORD']= host_list.password
            settings.DATABASES['users']['HOST']= host_list.host_name
            settings.DATABASES['users']['PORT']= host_list.port
            
            from users.models import test_tab
            try:
                all_obj_list = test_tab.objects.using('users').all()
            except Exception:
                all_obj_list = None
        
            if all_obj_list:
                print all_obj_list
        
        

        return None
