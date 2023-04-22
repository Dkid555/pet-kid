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


number = "23"
number = list(number)
number = [eval(i) for i in number]
n = len(number)

table = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

if __name__ == "__main__":
    print(Merge(number, n, table))
