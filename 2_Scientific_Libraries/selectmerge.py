import pandas as pd

names = ['Halley Fulp','Stephane Gries','Leah Lipp','Chae Keener','Adriana Lanigan']
cust_id = [33972,83013,38204,37730,57303]
order_no = [297207,262073,830364,118082,299700,277552,740047]
order_cust_id = [38204,33972,83013,38204,83013,80366,37730]

person = pd.DataFrame({'Name':names, 'CustomerId':cust_id})
order = pd.DataFrame({'OrderNo':order_no, 'CustomerId':order_cust_id})

person_order =pd.merge(person,order, on='CustomerId')
print(set(person_order.loc[:,'Name']))