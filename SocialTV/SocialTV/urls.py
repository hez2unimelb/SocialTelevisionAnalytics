from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^location_tweets/', 'SocialTV.views.locationTweets', name='locationTweets'),
     url(r'^day_comments/', 'SocialTV.views.commentDay', name='dayComments'),
     url(r'^hour_tweets/', 'SocialTV.views.tweetHour', name='hourTweets'),
     url(r'^day_tweets/', 'SocialTV.views.tweetDay', name='dayTweets'),
     url(r'^hour_reposts/', 'SocialTV.views.repostHour', name='hourReposts'),
     url(r'^day_reposts/', 'SocialTV.views.repostDay', name='dayReposts'),
     url(r'^hour_comments/', 'SocialTV.views.commentHour', name='hourComments'),
     url(r'^oneday_hour_tweets/', 'SocialTV.views.tweet24', name='oneDayHourTweets'),
          url(r'^triple/', 'SocialTV.views.triple', name='Triple'),
    url(r'^tests/', 'SocialTV.views.test', name='test'),
        url(r'^tests2/', 'SocialTV.views.test2', name='test2'),
        url(r'^$', 'SocialTV.views.home', name='home'),
        url(r'^tvprogram/', 'SocialTV.views.tvprogram', name='tvprogram'),
        url('program/(\d+)/','SocialTV.views.programDetail', name='program_detail'),
        url(r'^one_program/([A-Za-z]+)', 'SocialTV.views.oneProgram', name='oneProgram'),
        url(r'^keyword_cloud/', 'SocialTV.views.keywordCloud', name='keywordCloud'),
        url(r'^topic_bubble/', 'SocialTV.views.topicBubble', name='topicBubble'),
        url(r'^gender_pie/', 'SocialTV.views.genderPie', name='genderPie'),
        url(r'^verify_pie/', 'SocialTV.views.verifyPie', name='verifyPie'),
    # url(r'^SocialTV/', include('SocialTV.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
