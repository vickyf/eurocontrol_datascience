empnb = {'Brussels': 200, 'London': 52, 'New York': 45, 'Bejing': 20}
print('Paris' in empnb)
print(empnb['Brussels'])

emp = 0
for x in empnb: emp += empnb[x]
print (emp)