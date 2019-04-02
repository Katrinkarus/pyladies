
# PRVY DEN V CODECADEMY - 22.03.2019
# from datetime import datetime
# now = datetime.now()
# print('%02d/%02d/%04d ' '%02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))

# from datetime import datetime
# now = datetime.now()
# print('%02d:%02d:%04d' % (now.hour, now.minute, now.second))

# from datetime import datetime
# now = datetime.now()
# print('%02d/%02d/%04d' % (now.month, now.day, now.year))

# from datetime import datetime
# now = datetime.now()
# current_year = now.year
# print(current_year)
# current_month = now.month
# print (current_month)
# current_day = now.day
# print (current_day)

# from datetime import datetime
# now = datetime.now()
# print(now)

# day = 6
# print("03 - %s - 2019" % (day))
# print("03 - %02d - 2019" % (day))

# parrot = "Norwegian Blue"
# print(len(parrot))

# parrot = "Norwegian Blue"
# print(parrot.lower())

# parrot = "norwegian blue"
# print(parrot.upper()) 

# pi = 3.14
# print(str(pi))

print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print(original)
else:
  print("empty")