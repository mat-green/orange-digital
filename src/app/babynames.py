# -*- coding: utf-8 -*- 

'''
Created on Nov 4, 2013

@author: "Matthew Green<matthew@newedgeengineering.com>"
'''


import sys

from app.controls import Aggregator
from app.models import BabyName

program_usage = """USAGE:
babynames.py baby_name start_year end_year
Where:
 baby_name is your chosen name
 start_year is from 1880
 end_year is to 2010
        """


def main(argv=None):
    """Command line interface
%s
""" % program_usage

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)
    
    if(len(sys.argv) < 4):
        print(program_usage)
    else:
        baby_name = sys.argv[1]
        start_year = sys.argv[2]
        end_year = sys.argv[3]
        
        # Create model just to be tidy
        query = BabyName(baby_name, start_year, end_year)
        cmd = Aggregator(query)
        # simple connection check
        if(cmd.checkConnection()):
            print("please wait refreshing data")
            # refresh data
            cmd.refresh()
        # aggregate results
        average = cmd.calculateAverage()
        print("Between %s and %s the average popularity rank of the name %s was %.2f" % (start_year, end_year, baby_name, average))


if __name__ == '__main__':
    sys.exit(main())