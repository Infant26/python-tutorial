dict={0: {'name':'Anand', 'age': '24', 'salary':'paid'},
1: {'name':'infant', 'age': '23', 'salary':'paid'},
2: {'name':'Arun', 'age': '25', 'salary':'unpaid'},
3: {'name':'ajith', 'age': '28', 'salary':'paid'},
4: {'name':'prasad', 'age': '27', 'salary':'paid'},
5: {'name':'praveen', 'age': '24', 'salary':'unpaid'},
6: {'name':'saivignesh', 'age': '28', 'salary':'unpaid'},
7: {'name':'aravind', 'age': '43', 'salary':'paid'},
8: {'name':'balaji', 'age': '26', 'salary':'unpaid'}}
for i in range(9):
    #print(i)
    if(dict[i]['salary']=='unpaid'):
        print((dict[i]['name']))
#print (dict['emp4']['salary'])
