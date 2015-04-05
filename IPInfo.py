#!/usr/bin/python

# Author : Shirish Saxena
# Version : 8.8
# Email : me@shirish.me
# Copyright to Shirish [ me@shirish.me ] @ 2014


import sys
import json 
import urllib2
import time

def Get_Data(IP):
    start_time = time.time()
    url = 'http://ip-api.com/json/%s' %IP
    data = json.load(urllib2.urlopen(url))

    Status = data['status']

    if Status == 'success' :
        City = data['city']
        Zip = data['zip']
        CountryCode = data['countryCode']
        Country = data['country']
        Region = data['region']
        ISP = data['isp']
        Longitude = data['lon']
        Latitude = data['lat']
        TimeZone = data['timezone']
        AS = data['as']
        Query = data['query']
        Organization = data['org']
        RegionName = data['regionName']

        if not City :
            City = 'Unknown'
        if not Zip :
            Zip = 'Unknown'
        if not CountryCode:
            CountryCode = 'null'
        if not Country:
            Country = 'Unknown'
        if not Region :
            Region = 'Unknown'
        if not ISP :
            ISP = 'Unknown'
        if not TimeZone :
            TimeZone = 'Unknown'
        if not AS :
            AS = 'Unknown'
        if not Organization :
            Organization = 'Unknown'
        if RegionName :
            RegionName = 'Region                          : %s' %RegionName
        else:
            RegioName = ''

        print """

    IP                              : %s
    ISP                             : %s
    Country                         : %s (%s)
    City                            : %s
    Timezone                        : %s
    Zip                             : %s
    AS number/name                  : %s
    Organization                    : %s
    Longitude/Latitude              : %s/%s
    %s
	
    """ % (Query,ISP,Country,CountryCode,City,TimeZone,Zip,AS,Organization,Longitude,Latitude,RegionName)
        Time = time.time() - start_time
        Time = str(round(Time, 2))
        print ("    Time to Query                   : %s seconds" % Time)
    else :
        Error = data['message']
        Status = 'Fail'
        if Error == 'private range' :
            Error = 'Private Range'
            Description = 'The IP address is part of a private range'
        elif Error == 'reserved range' :
            Error = 'Reserved Range'
            Description = 'The IP address is part of a reserved range'
        elif Error == 'invalid query':
            Error = 'Invalid Query'
            Description = 'Invalid IP address or Domain name'
        elif Error == 'quota' :
            Error = 'Over Quota'
            Description = 'Over Quota'
        else :
            Error = data['message']
            Description = data['message']
        print '''
    Status                           : %s
    Error                            : %s ( %s )

    Description                      : %s

    ''' % (Status,Error,data['query'],Description)


while ( True ) :
    
    if len(sys.argv) > 1:
            IP = sys.argv[1]
            if IP == 'myip'  or IP == 'ip' or IP == 'ownip' or IP == 'system' or IP == 'systemip' :
                IP = ''
    else:
            print ''
            IP = raw_input('Enter IP/Hostname : ')
            if IP :
                if IP == 'myip'  or IP == 'ip' or IP == 'ownip' or IP == 'system' or IP == 'systemip' :
                    IP = ''
                    Get_Data( IP )
                elif IP == 'exit' or IP == 'quit' :
                    print 'Good Bye ! '
                    time.sleep(1)
                    quit
                    break
                else :
                    Get_Data( IP )
            
print ''
print "Created By Shirish Saxena | me@shirish.me"
print ''

