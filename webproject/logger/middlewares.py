from django.urls import resolve
import logging
import time
from datetime import datetime
from.models import RequestLog
from django.utils import timezone  
logger = logging.getLogger('middleware')
class LoggingMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        self.track_views = {
            'add'
        }
        print("🟢 MIDDLEWARE INITIALIZED!")

    def __call__(self,request):
        try:
            view_name = resolve(request.path).view_name
            if view_name in self.track_views:
                request.middleware_start_time = time.time()
                #self.handle_tracked_view(request,view_name)
        except:
            pass

        response =  self.get_response(request)

        if hasattr(request,'middleware_start_time') and view_name:
            duration = time.time() - request.middleware_start_time
            # if view_name == 'add_post':
            #     logger.info(f"⏱️ {view_name} took {duration:.3f} seconds")
        
            RequestLog.objects.create(
                view_name =view_name,
                method =request.method,
                duration =duration
            )
        return response
    
    # def handle_tracked_view(self,request,view_name):
    #     if view_name == 'add_post':
    #         self.log_post_creation(request)
    
    # def log_post_creation(self,request):
    #     if request.method == 'GET':
    #         logger.info(f"the starting time: {datetime.now()}")


    #     if request.method == 'POST':
    #         logger.info(f"the starting time: {datetime.now()}")


class GlobalContextMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response 
        self.site_name = "Logger Middleware"
    def __call__(self,request):
        request.global_context  = {
            'SITE_NAME': self.site_name,
            'Current_Time': timezone.now(),
        }
        print("🟢 GlobalContextMiddleware executed!")  # Debug
        return self.get_response(request)
    
