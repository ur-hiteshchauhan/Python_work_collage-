#WAP to combine list of words such that 1. similar indices combine together 2. each element of list1 combines with every element of list2  3. each element of list2 combine with every element of list1

list1 = ["apple","mango","banana"]
list2 = ["red","green","yellow"]

combined1 =[list1[i] + " --> " + list2[i] for i in range(len(list1))]

print(combined1)

