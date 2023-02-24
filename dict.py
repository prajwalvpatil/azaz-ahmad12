print("printing the dictionary items:")
dict1={"name":"azaz ahmad musalman","regno":366,"course":"Bca","age":20}
print(dict1)
print("accessing the items:")
print(dict1["age"])
print("using get():")
x=dict1.get("regno")
print(x)
print("changing hte values of dictionary:")
dict2={"regno":333}
dict1.update(dict2)
print(dict1)
print("lenth of the dictionary is b",len(dict1))