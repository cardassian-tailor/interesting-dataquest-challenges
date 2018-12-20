final_data = []
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

[final_data.append(x.split(',')) for x in rows]
'''
for item in rows:
    final_data.append(item.split(','))
    
print(final_data)

'''
