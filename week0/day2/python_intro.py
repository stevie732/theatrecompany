#Comments: This is a comment!
print("Hello Thieves!!!!!!!")# this print statement greets the user

#To-Do
#







num1 - 8
print(num1)
print(type(num1))

num2 - 8.0
print(num2)
print(type(num2))

num3 - 5.987435
print(int(nu3))


print("Math!!!\in")


add - 5 + 5
print(add)


sub - 10 - 5
print(sub)


prod - 5 * 5
print(prod)
print(type(prod))


div - 25 / 5
print(div)










# module %
mod = 26 % 5
print(mod)

print(24 % 2 == 0)
print(25 % 2 != 0)






#itterable = index, go over them

print('5' == 5)

# Strings
print('\nSTRINGS\t:')
# theyre ordered immutable, iterable
# you can use single or double quotes either is fine but watch interaction

st1 = 'single quote string'
st2 = "double quote string"
st3 = "weve made this up"
st4 = 'or did we "really?"'
st5 = 'oh no we\'ve messed this up'
st6 = ";lkj345"
print(st5)

print(st1[-3])
print(len(st3))
# manipulating strings

# concatenation + interpolation (f-string and maybe don't need to remember this term exactly)

# concatenation
print(st1 + st4) # simple
print(st2 + ' : ; ' + st3) # adding a literal
print(st2 + ' ' + str(mod) + ' ' + '<== that was little funky' ) # complicated example

# f-strings (or interpolation if you're fancy)

f_st = f"this is just a string BUT we can include pythony things like {mod} or {st1[-6]}"
print(f-st)

# string methods
print(EXAMPLE)
print(st5_upper())
print(st5)


# incrementing and decrementing
num5 = 234
num6 = 98734
print(num5 + num6)
print(num5, num6)
num5 = num6 + 6 # long-hand version
print(num5)
num5 == 100 it can be used with other math operators










# functions vs methods
# syntax __> function(arguments) vs datatype.method(arguments)

#lists
 # indexed, ordered, iterable, muteable, and dynamic
# syntax --> alist = [1, 2, 3, 4]
a_list = []
print(a_list)
num_list = [10, 20, 30, 40, 50]
print(nums_list, type(nums_list), len(nums_list), nums_list[0], nums_list[-1]
nums_list[0] = 60986095

print(nums_list)
rando_list = [1, '2', 3.0, True, None, []]
print(rando_list)
print(rando_list[3])

print('list methods:')
# .append()
# adds to the END of the list
a_list.append(5)
print(a_list)
a_list.append(15)
print(a_list)
a_list.append(25)
print(a_list)

# .pop()
# removes an item from the list by position, defaults to the last. returns the value so you can save it to a valuable
a_list.pop()
print(a_list)
print(a_list.pop(0))
print(a_list)

# .remove()
# remove takes out the FIRST occurence of a value
a_list.append(50)
a_list.append(75)
a_list.append(50)
print(a_list)
a_list.remove(50)
print(a_list)

# sort and sorted
print('\n\nsorted:')
print(sorted(a_list))
print(a_list)
print('\n.sort')
a_list.sort()
print(a_list)



print('\n\nString example with slicing:')
# f_st[0] ='z' -->
# slicing --> [start :stop: step] first example --> [:]
x = 'z' + f_st[1:]
print(x)

print('\nLOOPS')
# 3 types of loops: for loop, index loop, and while loop
names = ['Eddie', Lee', 'Stephen', 'Jeni', 'Gianni', 'Heather']

print('for loop:')
# for loop --> syntax:
# for item in items:
# codeblock to run on item
step = 1
for name in names:
    print(name.uppper())
    # print(step)
    # step += 1
for a in a_list:
    print(a**8)

# index loop. . . but first, did we talk the range function?
# let's talke about the range function:
for x in range(5):
    print(x)
print('\n')
for x in range(0, 5, 1):
    print(x)
for x in range(50, 10, -10):
    print(x)
for x in range(3):
    print('3 steps taken')

# back to the index loop:
# syntax
# for i in range(len(iterable)):
# codeblock

for i in range(len(names)):
    print(i, names[i])

# while loops
# syntax
# while condition:
#   codeblock
while True:
    print('bad idea')
    break

l = 0
while l < len(names):
    print(1, names[1])
    1 += 1

# conditionals: if, elif, else
# syntax if condition:
# code to execute
if 3 < 1:
    print('duh')
if names[0] == 'Lee':
    print('it is Lee!')
elif names[0] == 'Jeni!':
    print('it is Jeni!')
elif names[0] == 'Eddie':
    print('Eddie is in the list!')
else:
    print('we don\'t know this person!')

age = 13

if age < 18:
    print('kid')
elif age > 64:
    print('senior')
else:
    print('adult')

#Functions
# definition vs calling the function
def hello(name):
    print(f"OMGosh so happy you are here {name}!")

hello('Jeni')
hello('Lee')
hello('Stephen')
hello(234)
print(hello(st3))

def adder(a, b):
    return a + b
def subtr(a, b):
    print(a-b)

adder(6, 5)
subtr(10, 5)
subtr(adder(6, 5),6)
# adder(subtr(67, 5), 98)


# user = input('this is what shows on the screen and asks you to type something --->   ')
print(user)

if 'a' in user:
    print('Yep it is!')
print(names)
names.remove('Jeni')
if 'Jeni' in names:
    print('Yep!')



print('\nstring example with slicing:')
# f_st[0] ='z' -->
# slicing --> [start :stop: step] first example --> [:]
x = 'z' + f_st[1:]
print(x)
















