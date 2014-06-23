# -*- coding: utf-8 -*- 

'''
Created on Nov 4, 2013

@author: "Matthew Green<matthew@newedgeengineering.com>"
'''

import BeautifulSoup
import requests
import tempfile

from app.database import Sqlite
from app.models import Rank
import sys

database_location = '%s/babynames.db' % tempfile.gettempdir()
head_url = 'http://www.socialsecurity.gov/OACT/babynames/'
data_url = 'http://www.socialsecurity.gov/cgi-bin/popularnames.cgi'

class Aggregator(object):
    '''
    Controller that aggregates the bady name information.
    '''


    def __init__(self, query):
        '''
        Default Constructor
        
        :param query: BabyName model containing the data to find baby names.
        '''
        self.query = query
        try:
            db = Sqlite(database_location)
            db.build("rank", ["rank", "year", "name"], ["rank", "year", "name"])
        except:
            pass # already exists
        
        
    def checkConnection(self):
        '''
        Simple head check to see if the web site is available.
        '''
        result = requests.head(head_url)
        if(result.status_code == 200):
            return True
        else:
            return False
        
        
    def refresh(self):
        '''
        Data gather from web site.
        TODO: improve with async approach.
        '''
        db = Sqlite(database_location)
        
        for year in range(self.query.start, self.query.end+1):
            payload = { 'year': year, 'top': '1000', 'num': 'p' }
            result = requests.post(data_url, data=payload)
            if(result.status_code == 200):
                sys.stdout.write('.')
                sys.stdout.flush()
                dom = BeautifulSoup.BeautifulSoup(result.text)
                tables = dom.findAll("table")
                tablerows = tables[2].findAll("tr")
                for row in tablerows:
                    entries = row.findAll("td")
                    if(len(entries) == 3 and entries[1].text.lower() == self.query.name.lower()):
                        # persist in database
                        rank = Rank(entries[0].text, year, self.query.name)
                        rank.save(db)
        print('.')
        
                        
    def calculateAverage(self):
        '''
        Quick database lookup to determine the average rank.
        '''
        sql = """SELECT COUNT(*), SUM(rank)
                   FROM rank 
                  WHERE name='%s'
                    AND year BETWEEN %s AND %s
               GROUP BY name""" % (self.query.name, self.query.start-1, self.query.end+1)
        db = Sqlite(database_location)
        results = db.query(sql)
        return float(results[0][1])/float(results[0][0])
        
        