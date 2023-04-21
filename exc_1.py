#def cal(a,b,c):




def minus(Dict, Dict2, Minus):
    i = 0

    b = 0

    z = []

    f = []

    while i < len(Minus):

        while b < len(Dict):

            if Minus[i] == Dict[b]:

                #k = Dict.index(i)

                #z.append(Dict[b])

                #f.append(Dict2[b])

                Dict.pop(b)

                Dict2.pop(b)

                b -= 1

            b += 1

        i += 1

    #or i in z:

        #if (Dict)

     #   Dict.remove(i)

    #for i in f:

      #  Dict2.remove(i)   

    return Dict, Dict2

#

def plus(Dict, Dict2, PlusB, PlusA):

    L = []

    P = []
    i = 0

    b = 0

    while i < len(PlusB):

        z = 0

        while b < len(Dict):

            if PlusB[i] == Dict[b]:

                #k = Dict.index(b)

                Dict2[b] = PlusA[i]

                z = 0
            else:

                z+=1

            if z == len(Dict):

                L.append(PlusB[i])

                P.append(PlusA[i])#PlusB.index(i)])

                break

            b += 1

        b = 0

        i += 1

    for i in L:

        Dict.append(i)

    for i in P:

        Dict2.append(i)

    return Dict, Dict2






def splitbef(strng, sep, pos):

    strng = strng.split(sep)

    return sep.join(strng[:pos])

def splitaft(strng, sep, pos):

    strng = strng.split(sep)

    return sep.join(strng[pos:])



A = input().split()

Bef = []

Aft = []

for i in A:

    Bef.append(splitbef(i,'=',1))

    Aft.append(splitaft(i,'=',1))

C = []


B = int(input())
i = 0

while i < B:

        C.append(str(input()))

        i+=1

BefB = []

Aftminus = []

BefBB = []

AftBB = []

CC = []

for i in C:

    if i[0] == '-':

        Aftminus.append(splitaft(i, ' ', 1))

    if i[0] == '+':

        BefBB.append(splitbef(i[2:], ' ', 1))

        AftBB.append(splitaft(i[2:], ' ', 1))
       


for i in C:

    if i[0] == '-':

        Bef, Aft = minus(Bef, Aft, Aftminus)

    if i[0] == '+':

        Bef, Aft = plus(Bef, Aft, BefBB, AftBB)


K = str()
i = 0

while i < len(Bef):

    K = K + (Bef[i] + "=" + Aft[i]) + ' '

    i += 1


print(K.strip())




"""Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.


For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.


Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:


I can be placed before V (5) and X (10) to make 4 and 9. 

X can be placed before L (50) and C (100) to make 40 and 90. 

C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an intege"""


def change(lst):

    if lst == 'I':

        return 1

    if lst == 'V':

        return 5

    if lst == 'X':

        return 10

    if lst == 'L':

        return 50

    if lst == 'C':

        return 100

    if lst == 'D':

        return 500

    if lst == 'M':

        return 1000 


sm = 0

#i = 0
s = input()

lst = []

lst_int = []

lst.extend(s)
print(lst)
for i in lst:

    lst_int.append(change(i))

"""print(lst_int)"""
i = 0

if len(lst_int) == 1:
    print(lst_int[0])
    exit()
    """ 
    return lst_int[0]
    """


    


#hile 
else:

    while i < len(lst_int):
             

        if (i < len(lst_int) - 1) and lst_int[i] < lst_int[i+1]:

            sm = sm - lst_int[i]
        else:

            sm = sm + lst_int[i]

        i+=1
        


print(sm)




"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""

def Prefix(a):

    if len(a) == 1:
    
        return a[0]
    
    if len(a) == 0:
    
        return ""
    
    a.sort()

    size = len(a)



    end = min(len(a[0]), len(a[size - 1]))
    i = 0
    print(end)

    while (i < end and a[0][i] == a[size - 1][i]):
        i += 1
    
    return a[0][0: i]



strs = ["dog","racecar","car"]

print(Prefix(strs))


"""Find all triplets in list which sum is a zero"""

def Del(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n


def TripleF(lst, sum):
    lst.sort()
    #if len(lst) == 3:
    #    if lst[0]+lst[1]+lst[2] == 0:
     #       return lst
      #  else:
       #     return ""

    z = []
    List = []
    for i in range (0, len(lst) - 2):
        left = i + 1
        right = len(lst) - 1
        while left < right:
            if lst[i] + lst[left]+ lst[right] == sum:
                z.append(lst[i])
                z.append(lst[left])
                z.append(lst[right])
                List.append(z)
                z = []
                right = right - 1
                left = left - 1
            if lst[i] + lst[left]+ lst[right] < sum:
                left = left + 1
            else:
                right = right - 1
    return Del(List)

lst = [0,0,0]

print(TripleF(lst, 0))


"""Find sum of two numbers from list (target) and show their index (first that were finded)"""

def twoSum(nums, target):
    prevMap={} # - creation of dictionary {key: value} 
    for i,n in enumerate(nums): ## splits item from list on its index (i) and value (n)
            
        diff = target - n
        if diff in prevMap:
            return (prevMap[diff],i) # to find in dictionary we are using it keys
        prevMap[n]=i ## adding in dictionary new pair
    return
nums = [3,2,4]
target = 6
twoSum(nums, target)


"""or (works longer, On^2)"""
def Two_sum(lst, target):

    #nums.sort()
   # if lst[0] > target:
    #    return ""
    List = []
    for i in range(0, len(lst)-1):
        right = len(lst)-1
        k = target - lst[i]
        while right > i:
            if lst[right] == k:
                 List.append(i)
                 List.append(right)
                 return List
            right -= 1     

    return List

nums = [3,2,4,5,6]
target = 6
Two_sum(nums, target)

"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 s consists of parentheses only '()[]{}'
"""

def ClosingParen(s):
    lst=[]
    for par in s:
        if par == '{' or par == '[' or par == '(':
            lst.append(par)
        else:
            if not lst:
                return bool(None)
            else:
                top = lst[-1] # -1 - last element of sequence
                if (par == ')' and top == '(') or (par == ']' and top == '[') or (par == '}' and top == '{'):
                    lst.pop()
                else:
                    return bool(None)
    return lst

input1 = "{}}"
bool (ClosingParen(input1) == [])



""" Phone number merging letters"""

def Merge(number, n, table):
    lst = []
    q = []
    q.append("")
    while len(q) != 0:
        s = q.pop()
        if len(s) == n:
            lst.append(s)
        else:
            for letter in table[number[len(s)]]:
                q.append(s + letter)
    return lst            

number = ""
number = list(number)
number = [eval(i) for i in number]
n = len(number)

table = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

Merge(number, n, table)

"""Rotate numbers in list in k positions""" 

import collections


head = [1,2,3,4,5]
k = 2

head = deque(head)
i=0
while i < k:
    z = head.pop()
    head.appendleft(z)
    i+=1

print(head)



"""Unique Paths"""


import numpy as np

def Matrix(m, n):
    Mat = np.ones((m,n),int)
    i, j = 1, 1
    for i in range (1,m):
        for j in range (1,n):
            Mat[i][j] = Mat[i-1][j] + Mat[i][j-1]

    return Mat[m-1][n-1]


Matrix(20,20)    


"""OR"""
def Ones(m,n):
    
    Mat = [1] * n
    #Mat = np.ones((0,n),int)
    for i in range (1,m-1):
        for j in range (1,n):
            Mat[j] +=Mat[j-1]
    return Mat[n-1]

Ones(5,5)



"""Max profit (you can sell on each day)"""

def Prof(prices):
  
    profit = 0
    d = len(prices)
  
    for i in range(1, d):
  
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
  
    return profit

Prof(prices)


"""Max profit (find one best day to buy and one to sell)"""

import sys
prices = [7,1,5,3,6,4]
def Profit1(prices):
    maxprof = 0
    min_pr = sys.maxsize
    for i in range(0, len(prices)):
        if (min_pr > prices[i]):
            min_pr = prices[i]
        elif(prices[i] - min_pr > maxprof):
            maxprof = prices[i] - min_pr

    return maxprof

Profit1(prices)


"""123. Best Time to Buy and Sell Stock III
Hard
8K
155
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again)."""

prices = [7,1,5,3,6,4]

import sys
 
def maxtwobuysell(arr, size):
    first_buy = -sys.maxsize
    first_sell = 0
    second_buy = -sys.maxsize
    second_sell = 0
 
    for i in range(size):
 
        first_buy = max(first_buy, -arr[i])
        first_sell = max(first_sell, first_buy + arr[i])
        second_buy = max(second_buy, first_sell - arr[i])
        second_sell = max(second_sell, second_buy + arr[i])
 
     
    return second_sell


maxtwobuysell(prices, len(prices))


"""ListNode Del duplicates"""


def deleteDuplicates( head):
    """
        :type head: ListNode
        :rtype: ListNode
        """
    if not head:
        return head
    tail = head
    while tail.next:
        current = tail.next
        if current.val == tail.val:
            tail.next = current.next
        else:
            tail = current
    return head

ln=ListNode; l=ln(1, ln(1, ln(2, ln(3, ln(3)))))  
deleteDuplicates(l)  