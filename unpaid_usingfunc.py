def func1(t, s):
    if (d[t]['salary'] == 'unpaid'):
        return (t,s)
d={'emp1': {'name':'Anand', 'age': '24', 'salary':'paid'},
'emp2': {'name':'infant', 'age': '23', 'salary':'paid'},
'emp3': {'name':'Arun', 'age': '25', 'salary':'unpaid'},
'emp4': {'name':'ajith', 'age': '28', 'salary':'paid'},
'emp5': {'name':'prasad', 'age': '27', 'salary':'paid'},
'emp6': {'name':'praveen', 'age': '24', 'salary':'unpaid'},
'emp7': {'name':'saivignesh', 'age': '28', 'salary':'unpaid'},
'emp8': {'name':'aravind', 'age': '43', 'salary':'paid'},
'emp9': {'name':'balaji', 'age': '26', 'salary':'unpaid'}}
for k,v in d.items():
    #func1(k,v)
    str=func1(k,v)
    print(str)

