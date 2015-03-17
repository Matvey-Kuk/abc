from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from application.models import *
from django.http import HttpResponse
import json
from django.core import serializers
from django.http import HttpResponseRedirect
from django.db.models import Q
from operator import itemgetter
import threading
import time


class DelayedMessage(threading.Thread):

    def __init__(self,from_lead,to_lead, body, timeout):
        super(DelayedMessage, self).__init__()
        self.from_lead = from_lead
        self.to_lead = to_lead
        self.body = body
        self.timeout = timeout

    def run(self):
        time.sleep(self.timeout)
        message = Message()
        message.from_lead = self.from_lead
        message.to_lead = self.to_lead
        message.body = self.body
        message.save()


@csrf_exempt
def index(request):
    try:
        lead = Lead.objects.get(deviceId=request.GET.get('user_id'))
        return HttpResponseRedirect("chat?user_id=" + request.GET.get('user_id'))
    except Exception:
        lead = Lead()
        lead.deviceId = request.GET.get('user_id')
        lead.save()
    return render(request, 'index.html',)


@csrf_exempt
def get_messages(request):
    messages = Message.objects.filter(
        Q(to_lead__deviceId=request.POST.get('user_id')) | Q(from_lead__deviceId=request.POST.get('user_id')), id__gt=request.POST.get('last_message_id')
    )
    unread_messages_to_me = Message.objects.filter(to_lead__deviceId=request.POST.get('user_id'), has_been_read_by_receiver=False)
    for new_message in unread_messages_to_me:
        new_message.has_been_read_by_receiver = True
        new_message.save()

    return HttpResponse(serializers.serialize("json", messages), content_type="application/json")


def check_admin(request):
    return request.POST.get('admin_key') == "sdfjkhsg5dkfh4jgasd5kjhfgs435aLUF"


@csrf_exempt
def send_message(request):
    lead = Lead.objects.get(deviceId=request.POST.get('user_id'))
    admin = Lead.objects.get(is_admin=True)
    if not lead is None:
        message = Message()
        message.lead = lead
        print(request.POST.get('admin_key'))
        if check_admin(request):
            message.from_lead = admin
            message.to_lead = lead
        else:
            message.from_lead = lead
            message.to_lead = admin
        message.body = request.POST.get('text')
        message.save()
    return HttpResponse("ok")


@csrf_exempt
def get_contact_list(request):
    sorted_contacts = []
    contacts = []
    admin = Lead.objects.get(is_admin=True)
    if check_admin(request):
        leads = Lead.objects.filter(is_admin=False).all()
        for lead in leads:
            latest_message = Message.objects.filter(
                Q(to_lead=lead) |
                Q(from_lead=lead)
            ).latest('pk')

            new_message = False

            if(latest_message.to_lead == admin and not latest_message.has_been_read_by_receiver):
                new_message = True

            contacts.append({
                'lead_deviceId': lead.deviceId,
                'latest_message': latest_message.body,
                'new_message': new_message
            })

            sorted_contacts = sorted(contacts, key=itemgetter('new_message'))
            sorted_contacts = sorted_contacts[::-1]
    return HttpResponse(json.dumps(sorted_contacts), content_type="application/json")


def chat(request):
    try:
        lead = Lead.objects.get(deviceId=request.GET.get('user_id'))
        messages = Message.objects.filter(
            Q(to_lead__deviceId=request.GET.get('user_id')) | Q(from_lead__deviceId=request.GET.get('user_id'))
        )
        if len(messages) == 0:
            admin = Lead.objects.get(is_admin=True)

            message = Message()
            message.from_lead = admin
            message.to_lead = lead
            message.body = "Привет, друг! Меня зовут Антон и я с моей командой создал это приложение. Пока что мы не совсем закончили и очень не хотим тебя расстраивать чем-то неидеальным =)"
            message.save()

            new_message_thread1 = DelayedMessage(
                admin,
                lead,
                "Самое важное для меня -  это сделать не просто крутую программу, а нечто большее... Можешь рассказать, почему именно оно тебя заинтересовало и как ты хотел его использовать?",
                10
            )

            new_message_thread2 = DelayedMessage(
                admin,
                lead,
                "Если, конечно, есть немножко времени)",
                15
            )
            new_message_thread1.start()
            new_message_thread2.start()
    except Exception:
        return HttpResponseRedirect("?user_id=" + request.GET.get('user_id'))
    return render(request, 'chat.html')