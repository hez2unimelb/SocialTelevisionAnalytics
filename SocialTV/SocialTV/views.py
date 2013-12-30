from django.template import RequestContext
from django.shortcuts import render_to_response
from excel import ExcelReader
import random
from datetime import datetime
import time
from models import Program, Metric
from tables import ProgramTable
from django.shortcuts import render
from django_tables2   import RequestConfig
from mongodb import MongoReader
from tvDataLoader import tvDataLoader
import settings
import json
reader=ExcelReader('D:/academic/workspace/PythonTest/test/statistics.xlsx')
mgReader=MongoReader('')
tvReader=tvDataLoader(settings.STATIC_PATH+"/csvfile/list.json")
def locationTweets(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    #data=reader.getLocationTweets('Geographic')
    data=mgReader.getLocationData()
    context_dict = {'boldmessage': "I am bold font from the context"}
    context_dict= {'categories':data}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    
    return render_to_response('location_tweets.html', context_dict, context)
def dayComments(request):
    context = RequestContext(request)
    data=reader.getDayComment('Comment per day')
    columnName=['date','comments']
    reader.writeCSV('commentPerDay.csv', columnName, data)
    context_dict = {'boldmessage': "I am bold font from the context"}
    context_dict= {'categories':data}
    return render_to_response('day_comments.html', context_dict, context)
def hourTweets(request):
    context = RequestContext(request)
    data=reader.getHourTweets('Tweet per hour')
    columnName=['date','tweets']
  # reader.writeCSV('hourTweets.csv', columnName, data)
    context_dict = {'boldmessage': "I am bold font from the context"}
    context_dict= {'categories':data}
    return render_to_response('test.html', context_dict, context)
def dayTweets(request):
    context = RequestContext(request)
    data=reader.getDayComment('Tweet per day')
    columnName=['date','tweets']
    reader.writeCSV('dayTweets.csv', columnName, data)
    context_dict = {'boldmessage': "I am bold font from the context"}
    context_dict= {'categories':data}
    return render_to_response('day_tweets.html', context_dict, context)
def hourReposts(request):
    context = RequestContext(request)
    data=reader.getHourTweets('Repost per hour')
    columnName=['date','tweets']
    reader.writeCSV('hourRepost.csv', columnName, data)
    context_dict = {'boldmessage': "I am bold font from the context"}
    context_dict= {'categories':data}
    return render_to_response('hour_reposts.html', context_dict, context)
def dayReposts(request):
    context = RequestContext(request)
    data=reader.getDayComment('Repost per day')
    columnName=['date','tweets']
    reader.writeCSV('dayReposts.csv', columnName, data)
    context_dict = {'boldmessage': "I am bold font from the context"}
    context_dict= {'categories':data}
    return render_to_response('day_reposts.html', context_dict, context)
def hourComments(request):
    context = RequestContext(request)
    data=reader.getHourTweets('Comment per hour')
    columnName=['date','tweets']
    reader.writeCSV('hourComments.csv', columnName, data)
    context_dict = {'boldmessage': "I am bold font from the context"}
    context_dict= {'categories':data}
    return render_to_response('hour_comments.html', context_dict, context)
def oneDayHourTweets(request):
    context = RequestContext(request)
    data=reader.getHourTweets('24 hour division')
    columnName=['date','tweets']
    reader.writeCSV('oneDayHourTweets.csv', columnName, data)
    context_dict = {'boldmessage': "I am bold font from the context"}
    context_dict= {'categories':data}
    return render_to_response('test.html', context_dict, context)

def test(request):
    data=reader.getHourTweets('Comment per hour')
    xdata=[]
    ydata=[]
    for d in data:
        xtime=datetime.strptime(d[0], "%Y-%m-%d %H:%M:%S")        
        xdata.append(int(time.mktime(xtime.timetuple()) * 1000))
    for d in data:
        ydata.append(d[1])
#     start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
#     nb_element = 150
#     xdata = range(nb_element)
#     xdata = map(lambda x: start_time + x * 1000000000, xdata)
#     ydata = [i + random.randint(1, 10) for i in range(nb_element)]
#     ydata2 = map(lambda x: x * 2, ydata)

    tooltip_date = "%Y-%m-%d %H:%M:%S"
    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"},
                   "date_format": tooltip_date}
    chartdata = {'x': xdata,
                 'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie
                 }
   #              'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie}

    charttype = "lineWithFocusChart"
    chartcontainer = 'linechart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('test.html', data)
def test2(request):
    context = RequestContext(request)
    rawData=reader.getHourTweets('Comment per hour')
    for i in range(len(rawData)):
        xtime=datetime.strptime(rawData[i][0], "%Y-%m-%d %H:%M:%S")
        xtime=int(time.mktime(xtime.timetuple()) * 1000)
        rawData[i][0]=xtime
    context_dict= {'rawData':rawData}
    return render_to_response('test3.html', context_dict, context)
def home(request):
    programs=tvReader.getTvProgramNames()
    series=tvReader.getTvSeriesNames()
    return render(request,'main/index.html',{'pNames':programs,'sNames':series})
def tvprogram(request):
    if Program.objects.count()==0:
        Program.objects.create(name='Longmen Express', genre='Wuxia, comedy', link='http://wiki.d-addicts.com/Longmen_Express', updated='True')
    table=ProgramTable(Program.objects.all())
    RequestConfig(request).configure(table)
    if Metric.objects.count()==0:
        Metric.objects.create(name='Total Tweet volume',description='some items in transmission metrics,some items in transmission metrics')
        Metric.objects.create(name='Tweets per day',description='some items in transmission metrics,some items in transmission metrics')
        Metric.objects.create(name='Average TPM',description='some items in transmission metrics,some items in transmission metrics')
        Metric.objects.create(name='Peak TPM',description='some items in transmission metrics,some items in transmission metrics')
        Metric.objects.create(name='Average peak TPM',description='some items in transmission metrics,some items in transmission metrics')
        Metric.objects.create(name='Transmissions',description='some items in transmission metrics,some items in transmission metrics')
        Metric.objects.create(name='Average gender',description='some items in transmission metrics,some items in transmission metrics')
    return render(request, "main/tvprogram_overview.html", {"programs": table, "metrics": Metric.objects.all()})
def programDetail(request,args):
    hourTweetData=getData('Tweet per hour')
    dayTweetData=getData('Tweet per day')
    hourRepostData=getData('Repost per hour')
    dayRepostData=getData('Repost per day')
    hourCommentData=getData('Comment per day')
    dayCommentData=getData('Comment per day')
    htData=getData2('24 hour division')
    tripleData=getData3()    
    return  render(request, "main/program_detail.html", {'hourTweetData':hourTweetData, 'dayTweetData':dayTweetData, 'hourRepostData':hourRepostData, 'dayRepostData':dayRepostData,'hourCommentData':hourCommentData, 'dayCommentData':dayCommentData,'htData':htData,'tripleData':tripleData})
def getData(sheetName):
    rawData=reader.getHourTweets(sheetName)
    for i in range(len(rawData)):
        xtime=datetime.strptime(rawData[i][0], "%Y-%m-%d %H:%M:%S")
        xtime=int(time.mktime(xtime.timetuple()) * 1000)
        rawData[i][0]=xtime
    return rawData
def getData2(sheetName):
    rawData=reader.getHourTweets(sheetName)
    for i in range(len(rawData)):
        rawData[i][0]=rawData[i][0][:-6]
        rawData[i][1]=int(rawData[i][1])
    return rawData
def getData3(sheetName):
    rawData=reader.getTriple(sheetName)
    for i in range(len(rawData)):
        xtime=datetime.strptime(rawData[i][0], "%Y-%m-%d %H:%M:%S")
        xtime=int(time.mktime(xtime.timetuple()) * 1000)
        rawData[i][0]=xtime
    return rawData
def processData(rawData):
    for i in range(len(rawData)):
        xtime=datetime.strptime(rawData[i][0], "%Y-%m-%d %H:%M:%S")
        xtime=int(time.mktime(xtime.timetuple()) * 1000)
        rawData[i][0]=xtime
    return rawData
def tweetHour(request):
    data=processData(mgReader.getHourTweets())
    minDate=data[0][0]
    endItem=data.pop()
    maxDate=endItem[0]
    data.append(endItem)
    return  render(request, "main/charts/tweet_hour.html", {'hourTweetData':data, 'minDate':minDate, 'maxDate':maxDate})
def tweetDay(request):
    data=getData('Tweet per hour')
    return  render(request, "main/charts/keyword_cloud.html", {'dayTweetData':data})
def commentHour(request):
    data=processData(mgReader.getHourComments())
    minDate=data[0][0]
    endItem=data.pop()
    maxDate=endItem[0]
    data.append(endItem)
    return  render(request, "main/charts/comment_hour.html", {'hourCommentData':data, 'minDate':minDate, 'maxDate':maxDate})
def commentDay(request):
    data=getData('Comment per day')
    return  render(request, "main/charts/comment_day.html", {'dayCommentData':data})
def repostHour(request):
    data=processData(mgReader.getHourRepost())
    minDate=data[0][0]
    endItem=data.pop()
    maxDate=endItem[0]
    data.append(endItem)
    return  render(request, "main/charts/repost_hour.html", {'hourRepostData':data, 'minDate':minDate, 'maxDate':maxDate})
def repostDay(request):
    data=getData('Repost per day')
    return  render(request, "main/charts/repost_day.html", {'dayRepostData':data})
def tweet24(request):
    data=mgReader.getOneDayTweet()
    return  render(request, "main/charts/tweet_24.html", {'htData':data})
def triple(request):
    data=getData3('Triple')
    return  render(request, "main/charts/triple.html", {'tripleData':data})
def oneProgram(request,args):
    programs=tvReader.getTvProgramNames()
    series=tvReader.getTvSeriesNames()
    pData=tvReader.getProgramByName(args)
    sData=tvReader.getSeriesByName(args)
    data=pData is None and sData or pData
    mgReader.openTvDb(data['dbName'])
    name=data['name']
    description=data['description']
    return  render(request, "main/programs2.html", {'name':name, 'description':description, 'pNames':programs,'sNames':series})
def keywordCloud(request):
    data=mgReader.getKeywordCloud()
    return  render(request, "main/charts/keyword_cloud.html", {'keywordCloud':data})
def topicBubble(request):
    flare=open(settings.STATIC_PATH+"/csvfile/flare.json","w")
   # flare.write("Content-type: application/json; charset=utf-8\n")
    flare.write(mgReader.getTopics())
    return  render(request, "main/charts/topics.html")
def genderPie(request):
    data=mgReader.getGenderData()
    return  render(request, "main/charts/pie.html",{'pieData':data})
def verifyPie(request):
    data=mgReader.getVerifiedUserData()
    return  render(request, "main/charts/pie.html",{'pieData':data})