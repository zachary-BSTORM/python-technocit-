
my_list = {1:{"name":"John","age":30},2 : {"name":"Jane","age":30}}

# print(my_dict)

for k,v in my_list.items():
    print(f" k : {k} - name : {v.get("name")} - age : {v["age"]}")
    
dict.fromkeys((), value)