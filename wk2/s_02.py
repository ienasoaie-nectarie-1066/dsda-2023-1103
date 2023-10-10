from wk2 import functions as fun
import matplotlib.pyplot as plt

a = 5
b = 11
print(a, id(b))
print(b, id(a))
fun.swap(a, b)
print(a, id(b))
print(b, id(a))

a, b = fun.swap2(a, b)
print(a, b)
a, b = b, a
print(a, b)

# in python, parameters to functions/methods are passed by object reference
list_1 = [a, b]
fun.swap3(list_1)
print("l1 - ", list_1)


# List comprehension
list_2 = [x+1 for x in range(-10, 10)] # range(0, 10, 1)
print("l2 - ", list_2, type(list_2))

# extract from list_2 the positive values
# which are also even

list_3 = [x for x in list_2 if x > 0 and x % 2 == 0]
print("l3 - ", list_3)

list_4 = [1, 2, 3]
print("l4 - ", list_4)
# create a list with values from list_3 (x) and list_4 (y)
# in such a way that (x+y)**2 with x>4 and y%2!=0

list_5 = [(x+y)**2 for x in list_3 for y in list_4 if x >= 4 if y % 2 != 0]
print("l5 - ", list_5)

list_6 = [(x+y)**2 for x in list_3 for y in list_4]
print("l6 - ", list_6)

# create a list of pairs with one value from list_3 and one value
# from list_4

list_7 = [(x, y) for x in list_3 for y in list_4]
print("l7 - ", list_7)

# we end up with combinations of 2 values of 2 sets of data

# reading a text file as a list of lines
text_file = open('s_02.py', 'rt')
with text_file as f:
    for line in f:
        # print(line)
        # \n at the end of text line
        # exclude the last character
        print(line[:-1])
# dictionaries
dict_1 = {'monday': 'mama',
          'tuesday': 12.34,
          'wednesday': [1, 2, 3, 'tata', [4, 5]]}
print('dictionary - ', dict_1, type(dict_1))

# extract keys from dictionary
print(dict_1.keys(), type(dict_1.keys()))
print(list(dict_1.keys()), type(list(dict_1.keys())))
print(list(dict_1), type(list(dict_1)))

# extract values from dictionary
print(dict_1.values(), type(dict_1.values()))

# accessing the pairs of (k, v)
print(dict_1.items(), type(dict_1.items()))
for k, v in dict_1.items():
    print(k, ": ", v)

# dictionary comprehension
dict_2 = {x: (x+1)**2 for x in range(10)}
print(dict_2)

plt.plot(dict_2.keys(), dict_2.values())
# plt.show()

# create a dictionary with x key and values (x+y)**3
# with x in {0, ..., 50} and y in {0, ..., 100}
range_x = list(range(50))
print(range_x, type(range_x))
range_y = list(range(100))
print(range_y, type(range_y))

dict_3 = {x: (x+y)**2 for (x, y) in zip(range_x, range_y)}
print(dict_3)
plt.plot(dict_3.keys(), dict_3.values())
plt.show()
