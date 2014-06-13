class RequestDB(object):
    def process_request(self,request):
        print "Host" 
        host_str = request.get_host(SERVER_NAME)
        host_name = host_str.split(':')
        print host_str
        return None
