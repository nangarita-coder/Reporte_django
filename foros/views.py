from .logic import foros_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def foros_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            foro_dto = vl.get_foro(id)
            foro = serializers.serialize('json', [foro_dto,])
            return HttpResponse(foro, 'application/json')
        else:
            foro_dto = vl.get_foros()
            foros = serializers.serialize('json', foro_dto)
            return HttpResponse(foros, 'application/json')

    if request.method == 'POST':
        foro_dto = vl.create_foro(json.loads(request.body))
        foro = serializers.serialize('json', [foro_dto,])
        return HttpResponse(foro, 'application/json')

@csrf_exempt
def foro_view(request, pk):
    if request.method == 'GET':
        foro_dto = vl.get_foro(pk)
        foro = serializers.serialize('json', [foro_dto,])
        return HttpResponse(foro, 'application/json')

    if request.method == 'PUT':
        foro_dto = vl.update_foro(pk, json.loads(request.body))
        foro = serializers.serialize('json', [foro_dto,])
        return HttpResponse(foro, 'application/json')