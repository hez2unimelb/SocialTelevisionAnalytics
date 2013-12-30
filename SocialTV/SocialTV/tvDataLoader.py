import json
class tvDataLoader(object):

    def __init__(self, params):

        self.jsonFileLocation=params
        self.tvData=json.load(open(self.jsonFileLocation))
    def getTvProgramNames(self):
        data=[]
        for item in self.tvData['sub'][0]['sub']:
            if item['finished']=='True':
                data.append(item['name'])
        return data
    def getTvSeriesNames(self):
        data=[]
        for item in self.tvData['sub'][1]['sub']:
            if item['finished']=='True':
                data.append(item['name'])
        return data
    def getProgramByName(self,name):
        for item in self.tvData['sub'][0]['sub']:
            if item['name']==name:
                return item
    def getSeriesByName(self,name):
        for item in self.tvData['sub'][1]['sub']:
            if item['name']==name:
                return item
