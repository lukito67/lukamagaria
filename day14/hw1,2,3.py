set = set()
set.add(1)
set.add(2)
set.add(3)
set.add(4)
set.add(5)
print(set)




set2 =  {1,2,3,4,5,5,5,6,7,"python"}
set2.add("hello")
set2.remove("python")
print(set2)




set3 = {1,2,3,4,5,6,7,8,9,10}
list = []
for i in set3:
    if i % 2 == 0:
        list.append(i)

print(list)