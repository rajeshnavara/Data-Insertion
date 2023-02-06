from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def insert_topic(request):
    tn=input('Enter Topic Name :')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('Topic Inserted Successfully')

def insert_webpage(request):
    tn=input('Enter Topic Name:')
    name=input('Enter Your Name:')
    url=input('Enter Url Address :')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('Webpage Created Successfully')