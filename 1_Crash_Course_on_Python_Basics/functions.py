empnb = {'Brussels': 200, 'London': 52, 'New York': 45, 'Bejing': 20}
def cityList(dic):
    """This will return the total number of employees a company has from a dictionary
    with cities as keys and the numbers of employees in that city as its value."""
    lst=dic.values()
    s = 0
    for x in lst:
        s += x
    return s
print(cityList(empnb))