import json
import ast
import csv
import datetime
from dateutil.parser import parse


c=0
user=[]
import os
from glob import glob

result = [y for x in os.walk(os.getcwd()) for y in glob(os.path.join(x[0], '*.json'))]
writer = csv.writer(open("tweetsperday.csv", 'w'))
writer.writerow(["text","date"])




for elem in result:
  #  print (elem)

    tweets = []

    for line in open(elem, 'r'):

       # print(line)

        d = json.loads(line)
  #  break
        try:

                texto=  d['text']
                print(texto)
                dt = parse(d['created_at'])
                when = dt.strftime('%d/%m/%Y')
                print(when)
                concatenada = ([texto,when])
                writer.writerow(concatenada)



        except:
            print(d)
            pass





