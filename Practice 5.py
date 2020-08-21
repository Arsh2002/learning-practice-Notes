s= set()
print (type(s))
l =[1,2,3,4,5,6,]
s_from_list =set(l)
print (s_from_list)
print(type(s_from_list))
s.add(5)
s.remove(5)
s1= {4,6}
print(s.isdisjoint(s1))