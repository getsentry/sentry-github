from django.http import HttpResponse

from sentry.plugins.base import Response
from sentry.utils import json


# This is just a fixed version of sentry.plugins.base.JSONResponse
# that accepts a status kwarg
class JSONResponse(Response):
    def __init__(self, context, status=200):
        self.context = context
        self.status = status

    def respond(self, request, context=None):
        return HttpResponse(json.dumps(self.context),
                            content_type='application/json', status=self.status)
