#WAP to demonstrate replace , count , lenth, copy and reverse!!!

items = ["apple", "banana", "apple", "orange"]

items[1] = "mango"
print(items)
print(items.count("apple"))
print(len(items))
copied_items = items.copy()
print(copied_items)
items.reverse()
print(items)
