#making an empty dictionary
Dict = {} 
print(Dict)

#adding elements one at a time
Dict[0] = 'Good Morning'
Dict[2] = 'Sharlene'
Dict[3] = 69
print(Dict) 

#adding value set
Dict['Value_set'] = 8, 7, 3
print(Dict) 

#updating keys value
Dict[2] = 'Software Engineer'
print(Dict)

#nesting key value to dictionary
seven = 7
Dict[seven] = {'Nested': {'1' : 'Ciao', '2' : 'Software Engineers'}} 
print(Dict)