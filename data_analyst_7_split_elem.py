# From the data analyst track, section 7 in intro to python. 
# Splitting elements in a list. Here I used (on line 9) a generator instead of a for loop 

final_data = []
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

[final_data.append(x.split(',')) for x in rows]

'''
# This also works
for item in rows:
    final_data.append(item.split(','))
    
print(final_data)

'''
