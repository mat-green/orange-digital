# -*- coding: utf-8 -*- 

'''
Created on Nov 4, 2013

@author: "Matthew Green<matthew@newedgeengineering.com>"
'''

class BabyName(object):
    '''
    Model representing the query.
    '''

    def __init__(self, name, start_year, end_year):
        '''
        Default Constructor.
        
        :param name: The name of the male baby.
        :param start_year: The year to start looking for the name.
        :param end_year: The year to stop looking for the name, includes this 
            year.
        '''
        self.name = name
        self.start = int(start_year)
        self.end = int(end_year)
        
        
        
class Rank(object):
    '''
    Model representing the rank of name for a year
    '''
    
    def __init__(self, rank, year, name):
        '''
        Default Constructor.
        
        :param rank: The rank value of a name.
        :param year: The year of the rank.
        :param name: The baby name.
        '''
        self.rank = rank
        self.year = year
        self.name = name
        
        
    def save(self, database):
        '''
        Save model to database.
        
        :param database: Database to carry out persistence.
        '''
        database.save("rank", ["rank", "year", "name"], [self.rank, self.year, self.name])
        