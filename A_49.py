'''Write a Python script to concatenate following dictionaries to create 
a new one.'''
dict1={'dharti':5646, 'akash':9856, 'deep':8523}
dict2={'nitin':5214}
dict3={'poonam':9513, 'samarth':2034}
new_dict={}
new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)
print(new_dict)