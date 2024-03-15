from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):

    EFTO = TopicForm()
    d = {'EFTO': EFTO}
    if request.method=='POST':
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            tn = TFDO.cleaned_data['topic_name']
            TO =  Topic.objects.get_or_create(topic_name=tn)
            return HttpResponse('Topic Created')
        else:
            return HttpResponse('Invalid Data')

    return render(request, 'insert_topic.html', d)



def insert_webpage(request):
    EWFO = WebpageForm()
    d={'EWFO':EWFO}
    if request.method == 'POST':
        WFDO = WebpageForm(request.POST)
        if WFDO.is_valid():
            tn = WFDO.cleaned_data['topic_name']
            TO = Topic.objects.get(topic_name=tn)
            n = WFDO.cleaned_data['name']
            u = WFDO.cleaned_data['url']
            WO = Webpage.objects.get_or_create(topic_name=TO, name=n, url=u)[0]
            WO.save()
            return HttpResponse('Webpage Created')
        else:
            return HttpResponse('Invalid data')
    return render(request, 'insert_webpage.html', d)



def insert_accessrecord(request):
    EARFO = AccessRecordsForm()
    d = {'EARFO': EARFO}
    if request.method == 'POST':
        ARFDO = AccessRecordsForm(request.POST)
        if ARFDO.is_valid():
            wn = ARFDO.cleaned_data['name']
            WO = Webpage.objects.get(pk=wn)
            d = ARFDO.cleaned_data['date']
            a = ARFDO.cleaned_data['author']
            AO= AccessRecords.objects.get_or_create(name=WO, date=d, author=a)[0]
            AO.save()
            return HttpResponse('accessrecord reated')
        else:
            return HttpResponse('invalid data')
    return render(request, 'insert_accessrecord.html', d)


