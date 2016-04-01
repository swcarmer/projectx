# hello world, again

from datetime import date

today = date.today()
fool = date(today.year, 4, 1)

if today == fool:
    print "I pity the fool!"
else:
    print "Hello, world!"

 
