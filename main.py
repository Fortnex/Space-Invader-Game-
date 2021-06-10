
'''
import pywhatkit as mssg
import random

#Info about ppl

birthdays = {'Mathew': (28, 4, 2021)}
Numbers = {'Mathew':'+918156933600','Johans':'+91 85473 11420','Abel':'+971 55 279 3190', 'Enrique':'+91 98479 35403','Adam':'+968 9571 2743'} #Yet to save them

ppls ={'Aparna':''}

good_morning_wishes = ['Hey there, Mornin!','Good Morning','GM','Mornin to ya','Good morning starshine, the earth says Hello!','Morning, Whats good?']

import time as t

wish_choice = random.choice(good_morning_wishes)
print(wish_choice)
for name in Numbers:
    a = t.localtime()
    mssg.sendwhatmsg(Numbers[name],wish_choice,a.tm_hour,a.tm_min+1,wait_time=10)


#mssg.sendwhatmsg_to_group('3 Pixelated Musketeers','Morning yall',a.tm_hour,a.tm_min+1)



#mssg.sendwhatmsg('+971505243734',' this is an automated mssg douche',a.tm_hour,a.tm_min+1,wait_time=10)
    # #import subprocess
    #subprocess.call("taskkill /Im Edge.exe /f")
a = t.localtime()
mssg.sendwhatmsg('+971505243734',' a',a.tm_hour,a.tm_min+1,wait_time=10)
#mssg.sendwhatmsg('+91 81569 33600','a',a.tm_hour,a.tm_min+1,wait_time=10)
'''
from math import factorial

N=int(input("Enter"))

s=0
count=0
for i in range(1,N):
    a=str(i)
    print(a)
    for n in range(len(a)):
        s+=factorial(eval(a[n]))
        print(s)
    if s%i==0:
        print("\nYES\n")
        count+=1
print(count)