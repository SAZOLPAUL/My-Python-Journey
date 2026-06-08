#===============================
#Import modules and packages 
#===============================

#importing math and pi

import math
print(math.sqrt(9))


from math import sqrt,pi
print(sqrt(16))
print(sqrt(25))
print(pi)

#importing numpy

import numpy as np
print(np.array([1,2,3,4]))


from math import *
print(sqrt(64))
print(pi)

#importing array

import array
ary=array.array('i' , [1,2,3,4])
print(ary)

#importing random (.randint and .choice)

import random
print(random.randint(1,11))
print(random.choice(['apple', 'banana' , 'charry']))

#importing json

import json
data={'name':'sazol','age':19}

json_str=json.dumps(data)
print(json_str)
print(type(json_str))

parsed_data=json.loads(json_str)
print(parsed_data)
print(type(parsed_data))

#importing csv

import csv

with open('example.csv',mode='w',newline='') as file:
	writer=csv.writer(file)
	writer.writerow(['name','age'])
	writer.writerow(['sazol',19])
	
with open('example.csv',mode='r') as file:
	reader=csv.reader(file)
	for row in reader:
		print(row)
		
#importing datetime

from datetime import datetime,		timedelta

now=datetime.now()
print(now)

yesterday=now-timedelta(days=1)
print(yesterday)

import time
print(time.time())
time.sleep(5)
print(time.time())

#regular expresition

import re

pattern=r'\d+'
text='there are 123 apples 456'
match=re.search(pattern,text)
print(match.group())