#list 
list0=[1,3,9,80]
print(list0)
print(list0[-1],"length of the list is ",len(list0))
list1=[["ronit","paul"],["class","11","A"]];
print(list1[-2][-1])
list2=[]
list2.append(0)
list2.append(1)
list2.append(2)
list2.append(3)
print("---After appending---")
print(list2)
list2.extend([11,"ronit"])
print("---After etending---")
print("length of the list ",len(list2),list2)
print("---after inserting---")
list2.insert(0,"iomiop")
print(list2)
list2.reverse()
print("---after reversing---")
print(list2)
list2.remove(11)#element
print(list2)
list2.pop()
list2.pop(2)#index
print(list2)

list3=["krypto"]*4
print(list3)

