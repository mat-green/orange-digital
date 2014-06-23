'''
Created on Nov 4, 2013

@author: "Matthew Green<matthew@newedgeengineering.com>"
'''

import os
import sqlite3
import unittest

from app.database import Sqlite
import time

test_db = '/tmp/test.db'

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        if os.path.exists(test_db) and os.path.isfile(test_db):
            os.remove(test_db)


    def testBuildTable(self):
        # test set up
        component = Sqlite(test_db)
        # test execution
        component.build("test", [ "one", "two"])
        # test verification
        c = sqlite3.connect(test_db)
        cur = c.cursor()
        cur.execute("SELECT * FROM test")
        c.commit()
        c.close()
        
        
    def testSaveToTable(self):
        # test set up
        component = Sqlite(test_db)
        # test execution
        component.build("test", [ "one", "two" ])
        component.save("test", [ "one", "two" ], ["ooh", "laa"])
        # test verification
        c = sqlite3.connect(test_db)
        cur = c.cursor()
        cur.execute("SELECT * FROM test")
        result = cur.fetchone()
        self.assertEqual(result[0], "ooh")
        self.assertEqual(result[1], "laa")
        c.commit()
        c.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBuildTable']
    unittest.main()