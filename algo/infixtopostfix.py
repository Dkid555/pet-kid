operators = ['+', '-', '*', '/', '^', '(', ')']
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def inftopost(expression):
    lst = []
    out = ''
    for i in expression:
        if i not in operators:
            out += i
        elif i == '(':
            lst.append('(')
        elif i == ')':
            while lst and lst[-1] != '(':
                out += lst.pop()
            lst.pop()
        else:
            while lst and lst[-1] != '(' and priority[i] <= priority[lst[-1]]:
                out += lst.pop()
            lst.append(i)
    while lst:
        out += lst.pop()
    return out


if __name__ == "__main__":
    expression = input("Write expression (no dashes or spaces): ")
    print(inftopost(expression))
