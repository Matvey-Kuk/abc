from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from application.models import *
from django.http import HttpResponse
import json


@csrf_exempt
def index(request):
    try:
        lead = Lead.objects.get(deviceId=request.GET.get('user_id'))
    except Exception:
        lead = Lead()
        lead.deviceId = request.GET.get('user_id')
        lead.save()
    return render(request, 'index.html',)


@csrf_exempt
def get_messages(request):
    messages = Message.objects.filter(lead=request.GET.get('user_id'))
    return HttpResponse(json.dumps(messages), content_type="application/json")


def chat(request):
    return render(request, 'chat.html')