############################################
#Here you will find the Hackerrank code:####
############################################

############################################
#Introduction ##############################
############################################

#say "Hello, World!" with Python 
print("Hello, World!")
##################
#Python If-else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

if n%2 ==1:
    print("Weird")    
if n%2 == 0 and 2 <= n <= 5:
    print("Not Weird")
if n%2 == 0 and 6<= n <=20:
    print("Weird")
if n%2==0 and n> 20:
    print("Not Weird")
###################
#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)
####################
#python division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(int(a/b))
print(float(a/b))
######################
#loops
if __name__ == '__main__':
    n = int(input())
    
    for x in range(0,n):
        print(x*x)
######################
#write a function
def is_leap(year):
    leap = False
    not_leap = True
    # Write your logic here
    if year%400 == 0:
        return True
    if year%100 == 0:
        return False
    if year%4== 0:
        return True
    return leap
######################
#print a function
if __name__ == '__main__':
    n = int(input())
    
for x in range(1,n+1):
    print(x, end="")

############################################
#Basic Data Types ##########################
############################################
#Find the Runner-up Score
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    new_list = set(arr)
    new_list.remove(max(new_list))
    print(max(new_list))
########################
#nested lists
list1=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])

grades_list=sorted(list(set([student[1] for student in list1])))
second_grade=grades_list[1]

student_second=[
    student
    for student in list1
    if student[1]==second_grade
]

student_second.sort()
for student in student_second:
    print(student[0])
##################################
#finding the percentage 
if __name__ == '__main__':
    n = int(input())
    student_mark = {}
    for _ in range(n):
        name, *line = input().split()
        score = list(map(float, line))
        student_mark[name] = score
    query_name = input()
    mark = 0
    for x in student_mark[query_name]:
        mark=mark+x 
    result=mark/3
    print("%.2f"%result)
#################################
#lists
if __name__ == '__main__':
    N = int(input())
    my_list=[]
for x in range(N):
    k = input().split(" ")
    command= k[0]
    if command=="insert":
        my_list.insert(int(k[1]), int(k[2]))
    if command=="remove":
        my_list.remove(int(k[1]))
    if command=="append":
        my_list.append(int(k[1]))
    if command=="sort":
        my_list.sort()
    if command=="reverse":
        my_list.reverse()
    if command=="pop":
        if (len(my_list)!=0):
            my_list.pop()
    if command=="print":
        print(my_list)
#################################
#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t =tuple(integer_list)
    print(hash(t))
################################
#list comprehension
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = []
    list_ = []
    for k in range(x+1):
        for w in range(y+1):
            for q in range(z+1):
                if k+w+q != n:
                    list_ = [k,w,q]
                    result.append(list_)
    print(result)


############################################
#Strings ###################################
############################################
#sWAP cASE
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
################################
#string split and join 
def split_and_join(line):
    # write your code here
    a = line.split(" ")
    b = "-".join(a)
    return b
###############################
#what's your name?
def print_full_name(first, last):
    # Write your code here
    a = first
    b = last 
    c = ("Hello "+a+" "+b+"! You just delved into python.");
    print(c)
##############################
#mutations
def mutate_string(string, position, character):
    letters = list(string)
    letters[position] = character
    string = "".join(letters)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
##############################
#find a string
def count_substring(string, sub_string):
    counter=0
    for x in range(0, len(string)-len(sub_string)+1):
        if string[x] == sub_string[0]:
            counter_2=1
            for y in range (0, len(sub_string)):
                if string[x+y] != sub_string[y]:
                    counter_2=0
                    break
            if counter_2==1:
                counter += 1
    return counter
##############################
#string validators
if __name__ == '__main__':
    s = input()
    print(any([letter.isalnum()for letter in s]))
    print(any([letter.isalpha()for letter in s]))
    print(any([letter.isdigit()for letter in s]))
    print(any([letter.islower()for letter in s]))
    print(any([letter.isupper()for letter in s]))
############################
#text alignment 
thickness = int(input())
letter = "H"

for x in range(thickness):
    print((letter*x).rjust(thickness-1)+letter+(letter*x).ljust(thickness-1))

for y in range(thickness+1):
    print((letter*thickness).center(thickness*2)+(letter*thickness).center(thickness*6))

for z in range((thickness+1)//2):
    print((letter*thickness*5).center(thickness*6))    

for k in range(thickness+1):
    print((letter*thickness).center(thickness*2)+(letter*thickness).center(thickness*6))    

for w in range(thickness):
    print(((letter*(thickness-w-1)).rjust(thickness)+letter+(letter*(thickness-w-1)).ljust(thickness)).rjust(thickness*6))
#############################
#text wrap
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    my_list = textwrap.dedent(text=string) 
    result = wrapper.fill(text=my_list) 
    return result
##############################
#Designer door mat
N, M = map(int, input().split())
for x in range(1, N, 2):
    print(str('.|.' * x).center(M, '-'))
print('WELCOME'.center(M, '-'))
for y in range(N-2, -1, -2):
    print(str('.|.' * y).center(M, '-'))
##############################
#string formatting 
def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for x in range(1, number+1):
        decimal = str(x)
        octal = oct(x)[2:]
        hexadecimal = hex(x)[2:].upper()
        binary = bin(x)[2:]
    
        print(decimal.rjust(width),octal.rjust(width),hexadecimal.rjust(width),binary.rjust(width)) 
###########################
#alphabet rangoli
import string
def print_rangoli(size):
    # your code goes here
    import string
    design_formula = string.ascii_lowercase
    List = []
    for x in range(n):
        string = "-".join(design_formula[x:n])
        List.append((string[::-1]+string[1:]).center(4*n-3, "-"))
        
    print('\n'.join(List[:0:-1]+List))
###############################
#Capitalize!
# Complete the solve function below.
def solve(s):
    for x in s.split():
        s = s.replace(x,x.capitalize())
    return s
##############################
#the minion game
def minion_game(string):
    # your code goes here
    vowel = "AEIOU"
    sc = 0
    kc = 0
    x = len(string)
    for i in range(x):
        if string[i] in vowel:
            kc += x - i
        else:
            sc += x - i
    if sc > kc:
        print("Stuart", str(sc))
    elif kc > sc:
        print("Kevin", str(kc))
    else:
        print("Draw")
##############################
#Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    List = []
    for x in range(0, len(string), k):
        string_ = ""
        for y in string[x:x+k]:
            if y not in string_:
                string_ = string_ + y
        List.append(string_)
    print("\n".join(List))


############################################
#Sets ######################################
############################################
#Introduction to Sets
def average(array):
    # your code goes here
    assay_ = set(array)
    numerator = sum(assay_)
    denominator = len(assay_)
    solution = numerator/denominator
    return solution
#########################################
#No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT

n_m = input()
n = input().split()
A = input().split()
B = input().split()

A = set(A)
B = set(B)

happiness = 0
for x in n:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1
    
print(happiness)
#####################################
#simmetric difference 
# Enter your code here. Read input from STDIN. Print output to STDOUT
Folklore = int(input())
Fset = set(map(int, input().split()))
Evermore = int(input())
Eset = set(map(int, input().split()))

Fdef = Fset.difference(Eset)
Edef = Eset.difference(Fset)

output = Fdef.union(Edef)

for i in sorted(list(output)):
    print(i)
##################################
#set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
country = int(input())
country_list = set()
for x in range(country):
    country_list.add(input())

print(len(country_list))
##############################
#set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))

for x in range(int(input())): 
    s1 = input().split()
    if s1[0] == 'pop':
        s.pop()
    elif s1[0] == 'remove':
        s.remove(int(s1[1]))
    elif s1[0] == 'discard':
        s.discard(int(s1[1]))
print(sum(s))
############################
#Set .union()
# Enter your code here. Read input from STDIN. Print output to STDOUT

n_english = input()
english = input().split()
n_french = input()
french = input().split()
english = set(english)
french = set(french)

print(len(english.union(french)))
##############################
#set .intersection()
# Enter your code here. Read input from STDIN. Print output to STDOUT

n_english = input()
english = input().split()
n_french = input()
french = input().split()
english = set(english)
french = set(french)

print(len(english.intersection(french)))
###############################
#Set .difference()
# Enter your code here. Read input from STDIN. Print output to STDOUT

n_english = input()
english = input().split()
n_french = input()
french = input().split()
english = set(english)
french = set(french)

print(len(english.difference(french)))
#############################
#set .symmetric_difference()
# Enter your code here. Read input from STDIN. Print output to STDOUT

n_english = input()
english = input().split()
n_french = input()
french = input().split()
english = set(english)
french = set(french)

print(len(english.symmetric_difference(french)))
#############################
#Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT

n_set = int(input())
n_element_A = set(map(int, input().split()))
order_sets = int(input())

for x in range(order_sets):
    operation = input().split()
    if operation[0] == 'intersection_update':
        List = set(map(int, input().split()))
        n_element_A.intersection_update(List)
    elif operation[0] == 'update':
        List = set(map(int, input().split()))
        n_element_A.update(List)
    elif operation[0] == 'symmetric_difference_update':
        List = set(map(int, input().split()))
        n_element_A.symmetric_difference_update(List)
    elif operation[0] == 'difference_update':
        List = set(map(int, input().split()))
        n_element_A.difference_update(List)
    else :
        False

print(sum(n_element_A))
##############################
#The captain's room
# Enter your code here. Read input from STDIN. Print output to STDOUT

size_group = input()
list_rooms = input().split()
rooms = set(list_rooms)

for x in list(rooms):
    list_rooms.remove(x)

captain = rooms.difference(set(list_rooms)).pop()
print(captain)
###############################
#check subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
STDIN = int(input())
for x in range(STDIN):
    folklore = input()
    evermore = set(input().split())
    reputation = int(input())
    fearless = set(input().split())
    print(evermore.issubset(fearless))
###############################
#check strict superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
t = set(input().split())
input_ = int(input())
output = True

for x in range(input_):
    t2 = set(input().split())
    if not t2.issubset(t):
        output = False
    if len(t2) >= len(t):
        output = False

print(output)


############################################
#Collections ###############################
############################################
#Collectinos .counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

number_shoes = int(input())
size_shoes = collections.Counter(map(int, input().split()))

money = 0

for x in range(int(input())):
    shoe, price = map(int, input().split())
    if size_shoes[shoe]:
        money += price
        size_shoes[shoe] -= 1

print(money)
###########################################
#DefaultDict Tutorial 
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

N, M = map(int, input().split())
D = defaultdict(list)

for x in range(1, N + 1):
    D[input()].append(str(x))
for y in range(M):
    print(' '.join(D[input()]) or -1)
####################################
#collections .namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

n = int(input())
scol = ','.join(input().split())
Student = collections.namedtuple('Student',scol)

sum = 0
for x in range(n):
    row = input().split()
    student = Student(*row)
    sum += int(student.MARKS)

a = sum/n
print(a)
#####################################
#collections .orderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import*
a = int(input())
b = OrderedDict()
for x in range(a):
    item = input().split()
    itemPrice = int(item[-1])
    itemName = " ".join(item[:-1])
    if(b.get(itemName)):
        b[itemName] += itemPrice
    else:
        b[itemName] = itemPrice
for x in b.keys():
    print(x, b[x])
######################################
#word order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

ctr = Counter(input() for x in range(int(input())))
print(len(ctr))
print(*ctr.values())
####################################
#collections .deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
a = int(input())
b = deque()
for x in range(a):
    lst = list(input().split())
    if lst[0]=='append':
        b.append(int(lst[1]))
    elif lst[0]=='appendleft':
        b.appendleft(int(lst[1]))
    elif lst[0]=='popleft':
        b.popleft()
    elif lst[0]=='pop':
        b.pop()
for k in b:
    print(k,end=" ")
######################################
#company logo
from collections import Counter

logo = input()
sorted_logo = sorted(logo)

occurence = Counter(list(sorted_logo))

for x, y in occurence.most_common(3):
    print(x, y)
##################################
#Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
    
def cubes(x):
    while x:
        large = None
        if x[-1]>x[0]:
            large = x.pop()
        else:
            large = x.popleft()
        if len(x)==0:
            return "Yes"
        if x[-1]>large or x[0]>large:
            return "No"
            
            
for i in range(int(input())):
    T = int(input())
    d = deque(map(int,input().split()))
    print(cubes(d))


############################################
#Date and Time #############################
############################################
#Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

month,day,year = input().split()

week = {0:"MONDAY",
       1:"TUESDAY",
       2:"WEDNESDAY",
       3:"THURSDAY",
       4:"FRIDAY",
       5:"SATURDAY",
       6:"SUNDAY"}

day= int(day)
month= int(month)
year=int(year)

output = calendar.weekday(year,month,day)
print(week[output])
########################################
#time Delta
import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    time = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time)
    t2 = datetime.strptime(t2, time)
    return str(int(abs((t1-t2).total_seconds()))) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()



############################################
#Errors and Exceptions #####################
############################################
#Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)



############################################
#Built-ins #####################
############################################
#Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = input().split()

my_list = list()

for x in range(int(X)):
    list_2 = map(float, input().split())
    my_list.append(list_2)
    
for y in zip(*my_list): 
    print(sum(y)/len(y))
#########################################
#Athlete sort
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())


    ls=sorted(arr,key=lambda x:x[k])
    for y in range(len(ls)):
        for z in range(len(ls[y])):
            print(ls[y][z], end=' ')
        print()
###################################
#ginortS
inp = input()

def sor(k):
    letters = []
    digits = []
    for x in k:
        if x.isalpha():
            letters.append(x)
        else:
            digits.append(int(x))
     
    upper = []
    lower = []
    for w in letters:
        if w.isupper():
            upper.append(w)
        else:
            lower.append(w)
        
    even = []
    odd = []
    
    for z in digits:
        if z % 2 == 0:
            even.append(z)
        else:
            odd.append(z)
            
    upper = sorted(upper)
    lower = sorted(lower)
    even = sorted(even)
    odd = sorted(odd)
    
    result_letters = lower + upper
    result_numbers = odd + even
    
    return ''.join(result_letters) +''.join(map(str,result_numbers))
    
a = sor(inp)
print(a)


############################################
#Python Functinals #########################
############################################
#Map and Lambda functions
cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):

    sequence = [0, 1]
    
    for x in range(2, n):
        sequence.append(sequence[x-1] + sequence[x-2])
    
    return(sequence[0:n])


############################################
#Regex and Parsing #########################
############################################
#Detect float point number 
import re
from re import match, compile

pattern = compile('^[-+]?[0-9]*\.[0-9]+$')

for x in range(int(input())):
    print(bool(pattern.match(input())))
###########################################
#Re.split()
regex_pattern = r"[,.]"	# Do not delete 'r'.
########################################
#Group(), Groups() & GroupDict()
import re
S = input().strip()

pattern = re.search(r'([a-zA-Z0-9])\1', S)

if pattern:
    print(pattern.group(1))
else:
    print(-1)
#######################################
#Re.findall(), Re.finditer()
import re

S=input()
vowels='aeiou'

pattern = re.compile('[^{0}][{0}][{0}]+[^{0}]'.format(vowels), re.I)
match = pattern.search(S)

if not match:
    print('-1')
    
while match:
    print(S[match.start()+1:match.end() -1])
    match = pattern.search(S,match.start() +1)
#####################################
#Re.Start(), Re.end()
import re
s = input()
k = input()

pattern = re.compile(k)
match = pattern.search(s)

if not match:
    print('(-1, -1)')

while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(s, match.start() + 1)
####################################
#Validating Roman RNumerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.
####################################








############################################
#XML #######################################
############################################
#XML1 - Find the score
def get_attr_number(node):
    # your code goes here
    return len(node.attrib) + sum(get_attr_number(x) for x in node)
#########################################
#XML2 - Find the maximun depth
maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if (level == maxdepth):
        maxdepth += 1
    for x in elem:
        depth(x, level + 1)


############################################
#Closures and Decorators ###################
############################################
#standardize mobile numbers using decorators
def wrapper(f):
    def fun(l):
        # complete the function
        f(['+91 ' + x[-10:-5] + ' ' + x[-5:] for x in l])
    return fun



############################################
#Numpy #####################################
############################################
#Arrays
def arrays(arr):
    #complete this function
    # use numpy.array
    a = numpy.array(arr[::-1], float)
    return a
###################################
#shape and reshape
import numpy as np
arr = np.array(input().split(), int)
print(np.reshape(arr, (3,3)))
#######################################
#Transpose and Flatten
import numpy as np
N,M = map(int,input().split())
array = []
for x in range(N):
    row = list(map(int,input().split()))
    array.append(row)
final_array= np.array(array)
print(np.transpose(final_array))
print(final_array.flatten())
#############################
#concatenate
import numpy as np
N,M,P = map(int,input().split())
array_N = np.array([input().split() for x in range(N)],int)
array_M = np.array([input().split() for y in range(M)],int)
print(np.concatenate((array_N, array_M)))
####################################
#zeros and ones
import numpy as np
input_ = tuple(map(int,input().split()))
print(np.zeros(input_,int), np.ones(input_,int), sep='\n')
#####################################
#eye and identity
import numpy as np 
N,M = map(int,input().split())
np.set_printoptions(legacy="1.13")
print(np.eye(N,M))
#####################################
#array mathematics
import numpy as np
N,M = map(int,input().split())
N, M = (np.array([input().split() for _ in range(N)], int) for _ in range(2))
print(N+M)
print(N-M)
print(N*M)
print(N//M)
print(N%M)
print(N**M)
####################################
#floor, ceil and rint
import numpy as np
array = np.array(input().split(), float)
np.set_printoptions(legacy="1.13")
print(np.floor(array))
print(np.ceil(array))
print(np.rint(array))
####################################
#sum and prod 
import numpy as np
N, M = map(int, input().split())
arr = []
for x in range(N):
    arr.append(np.array(input().split(), int))
summ = np.sum(arr, axis=0)
print(np.prod(summ))
###################################
#min and max
import numpy as np
N, M = map(int, input().split())
arr = []
for x in range(N):
    arr.append(np.array(input().split(), int))
result = np.min(arr,axis=1)
print(np.max(result))
######################################
#dot and cross
import numpy as np
N = int(input())
arr1 = np.array([input().split() for x in range(N)], int)
arr2 = np.array([input().split() for y in range(N)], int)
print(np.dot(arr1, arr2))
#########################################
#inner and outer
import numpy as np
A = np.array(input().split(), int)
B = np.array(input().split(), int)
print(np.inner(A, B))
print(np.outer(A,B), sep="\n")
#########################################
#polynomials 
import numpy as np
P = np.array(input().split(), float)
x = int(input())
print(np.polyval(P, x))
#######################################
#linear algebra
import numpy as np
N = int(input())
arr = []
for x in range(N):
    row = np.array(input().split(), float)
    arr.append(row)
print(np.linalg.det(arr))
##########################################
#mean, var, std
import numpy as np
N, M = map(int, input().split())
arr = []
for x in range(N):
    arr.append(np.array(input().split(), int))
print(np.mean(arr, axis= 1))
print(np.var(arr, axis= 0))
std = (np.std(arr, axis= None))
std = round(std, 12)
print(std)
#########################################







