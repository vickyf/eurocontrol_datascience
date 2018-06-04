def first_n_projects(employee,n):
    it = iter(employee[3])
    i=0
    result =[]
    while i<n:
        try:
            result.append(next(it))
            i+=1
        except StopIteration:
            break
    return result

emp = ('John', 'Doe', 1970, ['Training', 'Project_X','Green Energy Project', 'Bicycle Project'], 'X')
emp2 = ('Jane', 'Doe', 1970, [], 'X')
print(first_n_projects(emp,2))
print(first_n_projects(emp,7))
print(first_n_projects(emp2,1))
