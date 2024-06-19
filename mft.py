#!/usr/bin/env python
#
from datetime import datetime
import sys
import operator

#include paths = sys.argv[1]

excludes = ['WinSxS', 'Inf','SysWOW64', 'Windows','Program Files','.lockbit']

myList = {}

# python mft.py file    stomp|tunnel "Users\user"
#               argv1   argv2        argv3 

#$STD_INFO can be modified by user level processes like timestomp.
#$FILE_NAME can only be modified by the system kernel. 

anomaly=""
anomalies={}
with open(str(sys.argv[1])) as f:
    for cur in f:
        if cur.startswith('0'):
            lines = [line for line in f]
            for each in lines:
                if str(sys.argv[2]) == 'stomp':
                    if "fn" in each.split('|')[9] and str(sys.argv[3]) in each and not any(x in each for x in excludes):
                        if ('b' in each[each.find('fn'):][4:8]):# and 'b' in each[each.find('si'):][4:8]):
                            pass
                        if ('b' in each[each.find('si'):][4:8]):# and not 'b' in each[each.find('fn'):][4:8]:
                            if not each.split('|')[11].strip() in myList:
                                myList[each.split('|')[11].strip()] = (each.split('|')[7] + ',' + each.split('|')[8] )  
                        elif  ('b' in each[each.find('fn'):][4:8]):
                            if each.split('|')[11].strip() in myList:
                                if (datetime.strptime(myList[each.split('|')[11].strip()].split(',')[0].strip()+' '+myList[each.split('|')[11].strip()].split(',')[1].strip(), '%Y-%m-%d %H:%M:%S.%f')  < datetime.strptime(each.split('|')[7].strip()+' '+each.split('|')[8].strip(), '%Y-%m-%d %H:%M:%S.%f')):
                                    print "ANOMALY---"
                                    print "\t" + each.split('|')[11].strip()
                                    print "\t$STD_INFO: " + str(myList[each.split('|')[11].strip()].split(',')[0] + myList[each.split('|')[11].strip()].split(',')[1])
                                    print "\t$FILE_NAME: " + each.split('|')[7].strip()+' '+each.split('|')[8].strip()
                                    if each.split('|')[7].strip() in anomalies:
                                        anomalies[each.split('|')[7].strip()] += 1
                                    else:
                                        anomalies[each.split('|')[7].strip()] = 1
                                    #myList[each.split('|')[11].strip()] = (each.split('|')[7] + ',' + each.split('|')[8] )
                    elif "si" in each.split('|')[9]:
                        if ('b' in each[each.find('si'):][4:8]):
                            if not each.split('|')[11].strip() in myList:
                                myList[each.split('|')[11].strip()] = (each.split('|')[7] + ',' + each.split('|')[8] )  
                elif str(sys.argv[2]) == 'tunnel':
                    if "si" in each.split('|')[9] and str(sys.argv[3]) in each:
                        if each[each.find('si'):][4:8] == '..c.':
                            anomaly = str(each.split('|')[2])
                            xTime = str(each.split('|')[7]) + ' ' + str(each.split('|')[8]) 
                            for z in lines:
                                if z.split('|')[0].strip() == anomaly.strip() and z[z.find('si'):][4:8] == 'mac.':
                                    zTime = str(each.split('|')[7]) + ' ' + str(each.split('|')[8])
                                    print("File Creation: " + '\t\t' + xTime)
                                    print("Parent Dir MFT change:  " + zTime)
        else:
            pass

sorted_x = sorted(anomalies.items(), key=operator.itemgetter(1))

print "\nSUMMARY...\n"
for each in sorted_x:
    print each                
                
