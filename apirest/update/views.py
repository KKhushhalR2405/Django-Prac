from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View



from .models import UpdateModel


def update_model_detail_view(request):
    data = {
        "count": 100,
        "content": "New content",
    }

    return JsonResponse(data)

class JsonCBV(View):

    def get(self,request, *args, **kwargs):
        data = {
            "count": 100,
            "content": "New content",
        }

        return JsonResponse(data)


class JsonResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(context,**response_kwargs)

    def get_data(self,context):
        return context 
