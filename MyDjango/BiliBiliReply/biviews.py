from django.shortcuts import render
from BiliBiliReply.models import bilibili

def reply(request):
    bilibilis=bilibili.objects.all()
    return render(request,'Reply.html',{'content':bilibilis})
