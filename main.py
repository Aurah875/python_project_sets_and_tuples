myTuple = ("Lucy","nelly", "victor", "Peter")
print(myTuple)
print(len(myTuple))  # checking the lenght of the tuple
for i in myTuple:  # looping through myTuple
    print(i)
if "Lucy" in myTuple: # checking for existence
    print("yes")
else:
    print("no")
print(myTuple.index('Lucy'))   # Tells the index of lucy.
mylist = list(myTuple)
print(mylist) # converts the list to tuple

y = (2, 34, 66, 77, 90)
z = (9, 29, 30, 28)
r = y+z
print(r) # adds the two tuples together.
b = y[2:5]
print(b) # slices the tuple y from the 2nd to the 5th value
x = y[2::]
print(y) # slices the tuple from the 2nd to the last value.
e = y[:-2] # chooses the second last value
print(y)
t = (3, 2, 5, 88, 99, 40, 56)
i1, *i2, i3 = t
print(i1)
print(*i2)
print(i3)
# SETS
foodstuffs = {"drinks", "fruits", "beverages", "breakfast", "grocery"}
print(foodstuffs)
for i in foodstuffs:
    print(i)
if "drinks" in foodstuffs:
    print("cocomelon")
else:
   print("yes")
print(foodstuffs.add("kales"))
print(foodstuffs.remove("drinks"))
odd = {1, 3, 5, 7, 9, 11}
even = {2, 4, 6, 8, 10, 12}
u = odd.union(even)
print(u)
i = odd.intersection(even)
print(i)
diff = even.difference(odd)
print(diff)
print(even.update(odd))
f = even.update(odd)
print(f)
seta = even.copy()
print(seta)
a = frozenset({5, 7, 8})
print(a)  # Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
