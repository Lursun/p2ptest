#coding:utf-8
import os
from django.shortcuts import render
from django.http import HttpResponse
from p2ptest.p2p import p2p
from p2ptest.message import message as message_module
import time



def JoinNode(request):
    p2p.P2PJoinStart((request.GET.get('ip','127.0.0.1'),int(request.GET.get('port','8001'))))
    return HttpResponse("JoinNode")

def send(request):
    print request.body
    msg="message:"+request.body+",\ntime:"+str(time.time())
    message_module.Message.send(msg)
    return HttpResponse(msg)