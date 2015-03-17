from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from application.models import *
from django.http import HttpResponse
import json
from django.core import serializers
from django.http import HttpResponseRedirect


@csrf_exempt
def index(request):
    try:
        lead = Lead.objects.get(deviceId=request.GET.get('user_id'))
        # return HttpResponseRedirect("chat?user_id=" + request.GET.get('user_id'))
    except Exception:
        lead = Lead()
        lead.deviceId = request.GET.get('user_id')
        lead.save()
    return render(request, 'index.html',)


@csrf_exempt
def get_messages(request):
    messages = Message.objects.filter(lead__deviceId=request.POST.get('user_id'), id__gt=request.POST.get('last_message_id'))
    new_messages = Message.objects.filter(lead__deviceId=request.POST.get('user_id'), hasBeenRead=False)
    for new_message in new_messages:
        new_message.hasBeenRead = True
        new_message.save()
    return HttpResponse(serializers.serialize("json", messages), content_type="application/json")


@csrf_exempt
def send_message(request):
    lead = Lead.objects.get(deviceId=request.POST.get('user_id'))
    if not lead is None:
        message = Message()
        message.lead = lead
        message.from_admin = False
        message.body = request.POST.get('text')
        message.save()
    return HttpResponse("ok")


def chat(request):
    return render(request, 'chat.html')