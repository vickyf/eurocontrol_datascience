employee = ('John', 'Doe', 1970, [])
print(employee[0])
employee[3].append('Project_X')
employee[3].insert(0,'Training')
print(len(employee[3]))
print('Project_Blue' in employee[3])
for x in employee[3]: print(x)
gen= ('X',)
empgen= employee + gen
print(empgen)