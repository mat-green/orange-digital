# Orange Digital - Cloud Software Engineer Tech Test #

## Introduction ##
Command line application that provides a way to find the top 1000 ranking male
names between two give years, i.e. Billy�between�1892�and�2001, of 1880�and�
2010.

## Execution ##

### Requisites ###
The following software is needed to execute this application:
* Python 2.6
* [virtualenv](http://pypi.python.org/pypi/virtualenv>)
* [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)

### Python Virtual Environment ###
We deploy this application into it's own virtual environment therefore you will 
need to do the same. Install & Activate the virtualenv (this assumes you are in 
the root of the application folder using a cli):

        easy_install virtualenv
        mkdir ~/.virtualenvs
        cd ~/.virtualenvs
        virtualenv orange
        source ~/.virtualenvs/orange/bin/activate

### Install Python Packages ###
This assumes you are in the root of the application folder using cli:

        cd src
        while read line; do easy_install -ZU $line; done < src/install-requires.txt
        while read line; do easy_install -ZU $line; done < src/install-test-requires.txt 
        
### Executing Unit Tests ###
This assumes you are in the root of the application folder using cli:

        cd src
        python setup.py develop
        nosetests
        
### Executing Query ###
This assumes you are in the root of the application folder using cli. The follow 
to be executed once to setup the application:

        cd src
        python setup.py develop
        
The following to be used to find information (assumes you are in the src folder):

        python app/babynames.py [name] [start year] [end year]
        
## Test Cases ##
* Billy�between�1892�and�2001: 202.29
* Jamie�between�1901�and�1987: 465.41
* Daniel�between�1996�and�1999: 10.75
* Neil�between�1957�and�1983: 185.22
* Jordan�between�1880�and�2010: 504.76
