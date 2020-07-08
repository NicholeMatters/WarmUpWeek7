afc = ['Pittsburgh Steelers', 'Cincinnati Bengals', 'Houston Oilers', 'Cleveland Browns', 'Jacksonville Jaguars']
print(afc)

print(afc[0])

print(afc.pop(3))

print(afc)

afc.append('Balimore Raven')

print(afc)

print("Take 2")

afc2 = {
  "Pittsburgh": "Steelers", 
  "Cincinnati": "Bengals", 
  "Houston": "Oilers", 
  "Cleveland" : "Browns", 
  "Jacksonville": "Jaguars"
  }
print(afc2)

# print(afc2[0])

print(afc2.pop("Cleveland"))

afc2.update({"Balimore" : "Raven"})

# afc["Balimore"] = "Ravens"

print(afc2)

print('Tuesday')

list = ['ant', 'apple', 'auto', 'allowed']

#alpha order
print(list)

#ordered the list by size
def Sorting(line): 
    sort = sorted(line, key=len) 
    return sort

print(Sorting(list)) 

# Class called city
# attributes
# Name (required)
# state(required)
# nickname(optional)
# Str -> <city name>, state
# Make an instance of this class for your city

class City: