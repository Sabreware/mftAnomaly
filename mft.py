from datetime import datetime
import sys

myList = {}

with open(str(sys.argv[1])) as f:
    for cur in f:
        if cur.startswith('0'):
            lines = [line for line in f]
            for each in lines:
                if "fn" in each.split('|')[9]:
                    if ('b' in each[each.find('fn'):][4:8] and 'b' in each[each.find('si'):][4:8]):
                        pass
                    if ('b' in each[each.find('si'):][4:8]):# and not 'b' in each[each.find('fn'):][4:8]:
                        if not each.split('|')[11].strip() in myList:
                            myList[each.split('|')[11].strip()] = (each.split('|')[7] + ',' + each.split('|')[8] )  
                    elif  ('b' in each[each.find('fn'):][4:8]):
                        if each.split('|')[11].strip() in myList:
                            if (datetime.strptime(myList[each.split('|')[11].strip()].split(',')[0].strip()+' '+myList[each.split('|')[11].strip()].split(',')[1].strip(), '%m/%d/%Y %H:%M:%S.%f')  > datetime.strptime(each.split('|')[7].strip()+' '+each.split('|')[8].strip(), '%m/%d/%Y %H:%M:%S.%f')):
                                print "ANOMALY---"
                                print "\t" + each.split('|')[11].strip()
                                print "\t$STD_INFO: " + str(myList[each.split('|')[11].strip()].split(',')[0] + myList[each.split('|')[11].strip()].split(',')[1])
                                print "\t$FILE_NAME: " + each.split('|')[7].strip()+' '+each.split('|')[8].strip()
                                #myList[each.split('|')[11].strip()] = (each.split('|')[7] + ',' + each.split('|')[8] )
                elif "si" in each.split('|')[9]:
                    if ('b' in each[each.find('si'):][4:8]):
                        if not each.split('|')[11].strip() in myList:
                            myList[each.split('|')[11].strip()] = (each.split('|')[7] + ',' + each.split('|')[8] )  
        else:
            pass
