##########################################
#birthday cake candles
##########################################
import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    a = []
    tallest = max(candles)
    for x in candles:
        if x == tallest:
            a.append(x)
            
    return len(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


##########################################
#Number Line Jumps
##########################################
import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    yes = "YES"
    no = "NO"
    if (x2 > x1 and v2 > v1) or (x1> x2 and v1 > v2):
        return no
    else:
        if v2-v1 == 0:
            return no
        else:
            if ((x1-x2) % (v2-v1)) == 0:
                return yes
            else:
                return no


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


##########################################
#Viral Advertising 
##########################################
import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    starting = 5
    result = 0

    for x in range(1,n+1):
        liked = int(starting/2)
        result += liked
        starting = liked*3
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


##########################################
#Recursive Digit Sum 
##########################################
import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    n = sum([int(n[x]) for x in range(len(n))]) * k
    return superDigit(str(n), 1) if n > 9 else n
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()



##########################################
#Insertion Sort 1 
##########################################
import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    f = arr[-1]
    
    for x in range(len(arr)-2, -1, -1):
        if arr[x] > f:
            arr[x+1] = arr[x]
            print(" ".join(map(str, arr)))
        else:
            arr[x+1] = f
            print(" ".join(map(str, arr)))
            break
    if arr[0] > f:
        arr[0] = f
        print(" ".join(map(str, arr)))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

##########################################
#Insertion Sort 2
##########################################
import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(start, arr):
    f = arr[start]
    
    for x in range(start-1, -1, -1):
        if arr[x] > f:
            arr[x+1] = arr[x]
        else:
            arr[x+1] = f
            break
    if arr[0] > f:
        arr[0] = f

def insertionSort2(n, arr):
    # Write your code here
    for y in range(1, len(arr)):
        insertionSort1(y, arr)
        print(" ".join(map(str, arr)))
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)



