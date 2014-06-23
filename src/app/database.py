'''
Created on Nov 4, 2013

@author: "Matthew Green<matthew@newedgeengineering.com>"
'''

import sqlite3

class Sqlite(object):
    '''
    classdocs
    '''


    def __init__(self, connection):
        '''
        Default Constructor.
        
        :param connection: The connection string for the database
        '''
        self.conn = connection
        
    
    def build(self, table, columns, keys=[]):
        '''
        Table builder.
        
        :param table: Name of table to create.
        :param columns: List of column names to be associate with the table.
        :param keys: Optional list of column names to be the primary key.
        '''
        if(len(keys) > 0):
            sql ='CREATE TABLE %s (%s, PRIMARY KEY (%s)) ' % (table, ','.join(columns), ','.join(keys))
        else:
            sql ='CREATE TABLE %s (%s)' % (table, ','.join(columns))
        c = sqlite3.connect(self.conn)
        cur = c.cursor()
        cur.execute(sql)
        c.commit()
        c.close()
    
    
    def save(self, table, columns, values):
        '''
        Data persistence.
        :param table: Name of table to persisted.
        :param columns: List of column names of the values to be persisted.
        :param values: List of values to be persisted.
        '''
        sql = 'INSERT OR REPLACE INTO %s(%s) VALUES(%s)' % (table, ','.join(columns), ','.join(('?' for i in range(len(columns)))) )
        c = sqlite3.connect(self.conn)
        cur = c.cursor()
        cur.execute(sql, values)
        c.commit()
        c.close()
        
        
    def query(self, sql):
        '''
        Free form query.
        :param sql: The SQL to be executed.
        :return: The rows retrieved.
        '''
        c = sqlite3.connect(self.conn)
        cur = c.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        c.commit()
        c.close()
        return result
    