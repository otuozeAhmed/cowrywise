# core modules
import datetime
import uuid

# local app modules
from django.core.cache import cache
from django.core.cache import caches

# 3rd party modules
from rest_framework.views import APIView
from rest_framework.response import Response


class Cowrywise(APIView):
    """This API returns unique UUIDs with their latest timestamps on each API call (i.e. reload)"""
    # I'm making this variable global to be accessible from anywhere. It holds my cached content,
    # which will subsequently add your API context to itself whenever it is called
    global context
    context = []

    def get(self, request, format=None):    
        # the current time you send a request to this API
        self.current_time = str(datetime.datetime.now())
        # randomly generated uuid4. note: even if you call this API at the same second,
        # its uuid will awalys be unique
        self.uuid_field = uuid.uuid4()
        # pass the above variables to a dictionary
        self._request = {self.current_time : self.uuid_field}
        # this will set a key called 'key' to every request on the cache. 
        # and sets the cache timeout to 4800 seconds
        cache.set('key', self._request, 4800)
        # This inserts the latest API call at the top of the list which is retrieved by its key
        context.insert(0, cache.get('key'))
        return Response(context)
