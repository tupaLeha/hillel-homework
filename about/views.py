import os

from django.http import HttpResponse
from django.shortcuts import render
from django_user_agents.utils import get_user_agent
import datetime


def whoami(request):
    browser = request.user_agent.browser.family
    ip = request.META['REMOTE_ADDR']
    time = datetime.datetime.now()
    return HttpResponse(f'Browser: {browser}, Ip adress: {ip}, Server time: {time}')


def source_code(request):
    f = open("about/views.py", 'r')
    text = str(f.readlines())
    f.close()

    return HttpResponse(text)



