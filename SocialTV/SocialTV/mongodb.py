from pymongo import MongoClient
import operator
import json
class MongoReader(object):
    def __init__(self, params):
        '''
        Constructor
        '''
        self.client=MongoClient('155.69.148.113',27017)
        
    def openTvDb(self,name):
        self.currentDb=self.client[name]
        self.hourDb=self.currentDb.my_time_distribution_hour
        self.locationDb=self.currentDb.my_province_distribution
        self.keywordDb=self.currentDb.my_keywords
        self.topicDb=self.currentDb.my_topics
        self.oneDayDb=self.currentDb.my_cum_time_distribution_hour
        self.userStatDB=self.currentDb.my_user_statistics
        
    def getHourData(self,columnName):
        data=[[]]
        for item in self.hourDb.find().sort('_id',1):
            vector=[]
            vector.append(str(item['_id']))            
            vector.append(item[columnName])
            data.append(vector)
        del data[0]
        return data
    def getHourData2(self):
        data=[[]]
        for item in self.hourDb.find().sort('_id',1):
            vector=[]
            vector.append(str(item['_id']))
            try:
                vector.append(item['comment_count'])
            except KeyError:
                vector.append(item['comment_sum'])
            data.append(vector)
        del data[0]
        return data          
    def getHourTweets(self):
        return self.getHourData('tweet_sum')
    
    def getHourComments(self):
        return self.getHourData2()
    
    def getHourRepost(self):
        return self.getHourData('repost_sum')
    def getLocationData(self):
        data=[[]]
        locationData=self.locationDb.find_one()
        sorted_locations = sorted(locationData.iteritems(), key=operator.itemgetter(1),reverse=True)
        for location in sorted_locations:
            vector=[]
            vector.append(location[0].encode('utf-8'))
            vector.append(locationData[location[0]])
            data.append(vector)
        del data[0]
        del data[0]
        return data
    def getKeywordCloud(self):
        data=[[]]
        keywordData=self.keywordDb.find_one()
        for keyword in keywordData.keys():
            if keyword=='##':
                continue
            vector=[]
            #vector.append(keyword.encode('utf-8'))
            vector.append(keyword)
            vector.append(keywordData[keyword])
            data.append(vector)
        del data[0]
        data.pop()
        return data
    def getTopics(self):
        data=[]
        for topic in self.topicDb.find():
            vector=[]
            for keyword in topic['keywords'].keys():
                wordSize=int((float(topic['keywords'][keyword])+1)*500)
                print wordSize
                vector.append({'name':keyword.encode('utf-8'), 'size':wordSize})
            data.append({'name':'topic '+str(topic['_id']), 'children':vector})
        finalData={'name':'flare', 'children':data}     
        return json.dumps(finalData,encoding="utf-8")
       
    def getOneDayTweet(self):
        data=[[]]
        oneDayData=self.oneDayDb.find_one()
        for time in oneDayData.keys():
            vector=[]
            vector.append(time)
            vector.append(oneDayData[time])
            data.append(vector)
        del data[0]
        data.pop()
        for item in data:
            item[0]=int(item[0])
        data.sort()
        return data
    def getGenderData(self):
        data=[]
        userData=self.userStatDB.find_one()
        for gender in userData['gender'].keys():
            data.append([str(gender),int(userData['gender'][gender])]) 
        return data
    def getVerifiedUserData(self):
        data=[]
        userData=self.userStatDB.find_one()
        for verify in userData['verified'].keys():
            data.append([str(verify),int(userData['verified'][verify])]) 
        return data
