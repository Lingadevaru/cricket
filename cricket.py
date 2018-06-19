from player_functions import batting, bowling

p1={'name':'Virat Kohli', 'role':'bat', 'runs':112, 'four':10, 'six':0, 'balls':119, 'field':0} 
p2={'name':'du Plessis', 'role':'bat', 'runs':120, 'four':11, 'six':2, 'balls':112, 'field':0} 
p3={'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10, 'runs':71, 'field':1} 
p4={'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10, 'runs':45, 'field':0} 
p5={'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34, 'field':0} 

arr1 = [p1, p2]
arr2 = [p3, p4, p5]

for dictionary in arr1:
    a = batting(dictionary)
    del dictionary['runs'], dictionary['four'], dictionary['six'], dictionary['balls'], dictionary['field'], dictionary['role']
    dictionary['batscore'] = a
    print(dictionary)

for dictionary in arr2:
    b = bowling(dictionary)
    del dictionary['runs'], dictionary['wkts'], dictionary['overs'], dictionary['role'], dictionary['field']
    dictionary['bowlcore'] = b
    print(dictionary)




