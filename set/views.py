#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from .models import *
from django.db.models import Count
import json

def json_response(func):
    """
    A decorator thats takes a view response and turns it
    into json. If a callback is added through GET or POST
    the response is JSONP.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = json.dumps(objects,default=json_serial)
            if 'callback' in request.REQUEST:
                # a jsonp response!
                data = '%s(%s);' % (request.REQUEST['callback'], data)
                return HttpResponse(data, "text/javascript")
        except:
            data = json.dumps(str(objects))
        return HttpResponse(data, "application/json")
    return decorator

def index(request):
    # cd={}
    # newswebsite = NewsWebsite.objects.all()
    # for nws in newswebsite:
    #     news = News.objects.filter(news_website_id=nws.news_website_id)
    #     conut = news.count()
    #     cd[nws.news_website_id]=conut
    # # first_newsw =NewsWebsite.objects.filter(news_website_id=1)
    # # fnw = NewsWebsite.objects.get(id==1)
    # # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # # output = ', '.join([p.name for p in first_newsw])
    # # output = output.join(fnw.name)
    # d = {'count':cd}
    return HttpResponseRedirect('/homepage.html/?navId=0')
    # return HttpResponse(first_newsw.name)

def homepage(request):
    return render(request,'homepage.html')
def parent(request):
    return render(request,'parent.html')
def sonEvent(request):
    return render(request,'sonEvent.html')
def test(request):
    return render(request,'test.html')
#第一个数组是banner，第二个是下面的新闻below_banner
@json_response
def getHomeNews(request):
    navId = request.GET.get('navId',0)
    data =[]
    # eventset=Event.objects.all().order_by('-event_datetime')[:50]
    # return eventset

    #!!临时修改
    # eventset=Event.objects.filter(normaleventtyperelative__normal_event_type_id=int(navId))[:50]
    # eventset=Event.objects.get(normaleventtyperelative__normal_event_type_id=int(navId))[:50].order_by('-event_datetime')


    # eventset=Event.objects.all()
    if(str(navId)=="0"):
        eventset=Event.objects.all().order_by('-event_datetime')[:50]
        banner,below_banner=getHomeData(eventset)
        data.append(banner)
        data.append(below_banner)
        return data
        # return HttpResponse(json.dumps(data,default=json_serial),content_type='application/json')
        # return HttpResponse(str(222))

    else:
        # eventset_sub = eventset.filter(normaleventtyperelative__normal_event_type_id=int(navId))
        eventset_sub = Event.objects.filter(normaleventtyperelative__normal_event_type_id=int(navId)).order_by('-event_datetime')[:50]
        banner,below_banner=getHomeData(eventset_sub)
        data.append(banner)
        data.append(below_banner)
        # netr_set = NormalEventTypeRelative.objects.filter(normal_event_type_id=int(navId))
        # for netr in netr_set:
        #     netr.event()
        return data
        # return HttpResponse(json.dumps(data,default=json_serial),content_type='application/json')




#根据event_set得到相应的banner 和 below_banner
def getHomeData(eventset):
    banner =[]
    for es in eventset[0:3]:
        a = es.toDICT()
        banner.append(a)
    # data.append(banner)
    below_banner=[]
    for esr in eventset[0:]:
        below_banner_sub=[]
        esrd= esr.toDICT()
        below_banner_sub.append(esrd)
        # 找子事件
        pre_event_set = esr.pre_event.all()
        count = pre_event_set.count()
        if count !=0:
            for pes in pre_event_set[0:2]:
                pesd = pes.later_event.toDICT()
                below_banner_sub.append(pesd)
        below_banner.append(below_banner_sub)
    # data.append(below_banner)
    # return HttpResponse(json.dumps(data,default=json_serial),content_type='application/json')
    return banner,below_banner


@json_response
def getNavs(request):
    data =[]
    normal_event = NormalEvent.objects.all()
    for ne in normal_event:
        ne_content={}
        ne_content["normal_event_type_id"]= ne.normal_event_type_id
        ne_content["normal_event_type_name"]= ne.normal_event_type_name
        data.append(ne_content)
    # return HttpResponse(json.dumps(data),content_type='application/json')
    return data

@json_response
def getBannerAndCharts(request):
    eventid = request.GET.get('newsId',1)
    data=[]
    eventarray=[]   #第一个数组，事件数组
    event = Event.objects.get(event_id=eventid)
    event_dict = event.toDICT()
    eventarray.append(event_dict)   #把主事件添加到第一个数组
    pre_event_set = event.pre_event.all()
    #最大事件的新闻来源比例
    newssource_dict=getNewssource(eventid)
    #最大事件的情绪分布比例
    emotion_dict = getEmotion(eventid)
    #折线图未实现
    linechart=[]
    #有子事件的大事件
    if pre_event_set.count() != 0:

        for pes in pre_event_set:
            #子事件的新闻来源比例
            newssource_sub = getNewssource(pes.later_event_id)
            for key,value in newssource_sub.items():
                newssource_dict[key]=float(newssource_dict[key])+float(value)
            #将所有子事件添加到第一个数组上
            pesd = pes.later_event.toDICT()
            eventarray.append(pesd)
            #子事件的情绪分布比例
            emotion_sub = getEmotion(pes.later_event_id)
            for key,value in emotion_sub.items():
                emotion_dict[key]=float(emotion_dict[key])+float(value)
            #子事件的评论数


        data.append(eventarray)
        data.append(linechart)

        event_total_sum = pre_event_set.count()+1
        allnewssource=[]        #所有新闻来源比例
        allemotion=[]        #所有新闻来源比例
        #计算所有新闻来源比例
        for key,value in newssource_dict.items():
            newsarray=[]
            newsarray.append(key)
            v =value/event_total_sum
            newsarray.append(("%.2f" % v))
            allnewssource.append(newsarray)
            # newssource_dict[key]
        data.append(allnewssource)
        #计算所有情绪分布比例
        for key,value in emotion_dict.items():
            newsarray=[]
            newsarray.append(key)
            v=value/event_total_sum
            newsarray.append(("%.2f" % v))
            allemotion.append(newsarray)
            # newssource_dict[key]
        data.append(allemotion)

#没有子事件的大事件
    else:

        data.append(eventarray)
        data.append(linechart)
        allnewssource=[]
        for key,value in newssource_dict.items():
            newsarray=[]
            newsarray.append(key)
            newsarray.append(value)
            allnewssource.append(newsarray)
            # newssource_dict[key]
        data.append(allnewssource)
        allemotion=[]
        for key,value in emotion_dict.items():
            newsarray=[]
            newsarray.append(key)
            newsarray.append(value)
            allemotion.append(newsarray)
            # newssource_dict[key]
        data.append(allemotion)


    news_set = News.objects.filter(eventnewsrelative__event_id=eventid)
    q = news_set.values('news_website_id').annotate(Count('news_website_id'))
    totalnum = news_set.count()
    news_website_dict = {}
    for a in q:
        news_website_id = a['news_website_id']
        NewsWebsite.objects.get(news_website_id=news_website_id)
    # event_news_set = EventNewsRelative.objects.filter(event_id=eventid)
    # news_set = event_news_set.news()

    return data
    # return HttpResponse(json.dumps(data,default=json_serial),content_type='application/json')
#根据事件的id获取其评论数
def getCommentnum(eventid):
    totalnum=0
    news_set = News.objects.filter(eventnewsrelative__event_id=eventid)
    for ns in news_set:
        news_comment_set_sub = ns.newscomment_set.all()
        num_sub = news_comment_set_sub.count()
        totalnum+=num_sub
    return totalnum
#根据事件号获取新闻来源比例
def getNewssource(eventid):
    #新闻来源比例
    newssource=[]
    news_website_dict={}
    news_website_set = NewsWebsite.objects.all()
    for nws in news_website_set:
        news_website_dict[nws.name]=0
    news_set = News.objects.filter(eventnewsrelative__event_id=eventid)
    # news_set = News.objects.all()
    totalnum = news_set.count()
    q = news_set.values('news_website_id').annotate(Count('news_website_id'))
    news_website_array=[]
    for a in q:
        newsarray=[]
        news_website_id = a['news_website_id']
        news_website_name = NewsWebsite.objects.get(news_website_id=news_website_id).name
        news_website_num = a['news_website_id__count']
        if totalnum==0:
            b=0
        else:
            b = float(news_website_num)*100/totalnum
        bi = ("%.2f" % b)
        bf = float(bi)
        news_website_dict[news_website_name]+=float(bi)
        # newsarray.append(news_website_name)
        # newsarray.append(bi)
        # news_website_array.append(newsarray)
    for nws in news_website_set:
        news_website_dict[nws.name]=str(news_website_dict[nws.name])
    return news_website_dict
    # for key,value in news_website_dict.items():
    #     newsarray=[]
    #     newsarray.append(key)
    #     newsarray.append(("%.2f" % value))
    #     news_website_array.append(newsarray)
    # event_news_set = EventNewsRelative.objects.filter(event_id=eventid)
    # news_set = event_news_set.news()
    # return HttpResponse(json.dumps(news_website_array,default=json_serial),content_type='application/json')
    # return news_website_array
#根据事件号获取其所有评论的情绪比例
def getEmotion(eventid):
    # news_set = News.objects.filter(eventnewsrelative__event_id=1)
    news_set = News.objects.filter(eventnewsrelative__event_id=eventid)
    #根据数据库情绪的种类构造情感词典
    emotion = Emotion.objects.all()
    emotion_num_dict = {}
    for a in emotion:
        emotion_num_dict[a.emotion_name]=0

    totalnum=0
    for ns in news_set:
        news_comment_emotion_set = ns.newscommentemotionrelative_set.all()
        totalnum += news_comment_emotion_set.count()
        q = news_comment_emotion_set.values('emotion_id').annotate(Count('emotion_id'))
        for i in q :
            emotion_id = i['emotion_id']
            emotion_name = Emotion.objects.get(emotion_id=emotion_id).emotion_name
            emotion_num_dict[emotion_name]+=i['emotion_id__count']

    emotion_bi=[]
    for key,value in emotion_num_dict.items():
        emotionarray=[]
        emotionarray.append(key)
        if totalnum==0:
            b=float(0)
        else:
            b = float(value)*100/totalnum
        bi = ("%.2f" % b)
        bf = float(bi)
        emotionarray.append(bf)
        emotion_num_dict[key]=bi
        emotion_bi.append(emotionarray)
    return emotion_num_dict
    # return HttpResponse(json.dumps(emotionarray,default=json_serial),content_type='application/json')

        # for ncs in news_comment_emotion_set:
        #     news_comment_emotion = ncs.newscommentemotionralative_set.all()
@json_response
def getKeywordAndComment(request):
    eventid = request.GET.get('newsId',3)
    kwac=[]
    event_keyword_relative_set = EventKeywordRelative.objects.filter(event_id=eventid)
    event_keyword_relative_array = []
    for ekrs in event_keyword_relative_set:
        eka=[]
        key_name = ekrs.word.word_content
        key_weight = ekrs.word_weight
        eka.append(key_name)
        eka.append(key_weight)
        event_keyword_relative_array.append(eka)
    news_set = News.objects.filter(eventnewsrelative__event_id=eventid)
    comment = []
    for ns in news_set:
        news_comment_set = ns.newscomment_set.all()
        for ncs in news_comment_set:
            ncsdict = ncs.toDICT()
            # ncsdict["news"]=
            comment.append(ncsdict)
    kwac.append(event_keyword_relative_array)
    kwac.append(comment)
    # kwac.append(len(comment))
    # return HttpResponse(json.dumps(kwac,default=json_serial),content_type='application/json')
    return kwac
@json_response
def ajax_list(request):
    a = range(100)
    return a
    # return HttpResponse(json.dumps(a), content_type='application/json')

@json_response
def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return name_dict
    # return HttpResponse(json.dumps(name_dict), content_type='application/json')

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial[:10]
    # raise TypeError ("Type not serializable")