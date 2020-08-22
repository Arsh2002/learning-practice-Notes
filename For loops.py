list1=[["arsh",1],["prem",25],["yugal",3],["basit",40],["munaf",665]]
dict1 =dict(list1)

#for item in dict1:
#    print(item)
for item,choclate in dict1.items():
    print (item,'and choclate is',choclate)
items = [int, float, "HaERRY", 5, 3, 3, 22, 21, 64, 23, 233, 23, 6]
for item in items:
    if int(item).isnumeric() and item >= 6:
        print(item)

