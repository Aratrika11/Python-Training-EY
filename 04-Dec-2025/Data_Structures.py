"""6. Given a list of product prices, remove duplicates while maintaining order.

prices = [500,1000,3000,1500,500,3000]
distinct_prices = []
for p in prices:
    if p not in distinct_prices:
        distinct_prices.append(p)
print("After Duplicate Removal\n")
print(distinct_prices)"""

"""7. Merge two lists into a dictionary of {key: value} where list1 is keys and list2 is values.

list1 =["Apple","Orange","Banana"]
list2 =[1,2,3]
result = {}
for i in range(len(list1)):
    key = list2[i]
    value = list1[i]
    result[key] = value
print("Merged\n")
print(result)"""

"""8.Given a dictionary of student marks, return the top 3 students.

marks = {"Aratrika":98,"Nirakshi":90,"Titli":88,"Bidita":95}
top_three = sorted(marks.items(), key= lambda x: x[1], reverse = True)[:3]
print("The top 3 students are\n")
print(top_three)"""

"""9. Flatten a nested list like [[1,2],[3,4],[5,6]] into a single list.
l1 = [[1,2],[3,4],[5,6]]
fl =[]
for i in l1:
    for j in i:
        fl.append(j)
print("Flattened list\n")
print(fl)"""

"""10. Find common elements between three sets.
s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}
common =s1&s2&s3
print("Common Element: ",common)"""

"""11. Convert a list of tuples to a dictionary only if keys are unique.

lt = [("apple",1),("banana",2),("orange",3)]
keys = [k for (k,v) in lt]
if len(keys) == len(set(keys)):
    result = dict(lt)
    print(result)
else:
    print("Error: Keys are not unique")"""

"""12. Given a tuple of names, return one tuple with unique names.

names = ["Aratrika","Nirakshi","Titli","Aratrika"]
unique_names = []
for name in names:
    if name not in unique_names:
        unique_names.append(name)
unique_names = tuple(unique_names)
print("Unique names:\n",unique_names)"""

"""13. Build a program to reverse every alternate element in a list.

l = [1,3,5,7,9,11,13]
for i in range(0,len(l),2):
    l[i]=l[i]
for i in range(1,len(l),2):
    l[i]=-l[i]
print(l)"""

"""14. From a dictionary of employees, filter only employees with salary above 60000.

employees = {
    "Aratrika":75000,
    "Nirakshi":60000,
    "Titli":70000,
    "Bidita":80000,
}
high_salary = {}
for name,salary in employees.items():
    if salary > 60000:
        high_salary[name] = salary
print("Filtered")
print(high_salary)"""

"""15. Given two dictionaries, combine them but sum values for matching keys.
d1 = {"a":10,"b":20,"c":30}
d2 = {"a":15,"c":35,"d":40}
result = {}
for k in d1:
    result[k] = d1[k] + d2.get(k,0)
for k in d2:
    if k not in result:
        result[k]=d2[k]
print(result)"""