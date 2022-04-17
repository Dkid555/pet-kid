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


