"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 s consists of parentheses only '()[]{}'
"""


def closingParen(s):
    lst = []
    for par in s:
        if par == '{' or par == '[' or par == '(':
            lst.append(par)
        else:
            if not lst:
                return bool(None)
            else:
                top = lst[-1]  # -1 - last element of sequence
                if (par == ')' and top == '(') or (par == ']' and top == '[') or (par == '}' and top == '{'):
                    lst.pop()
                else:
                    return bool(None)
    return lst


if __name__ == "__main__":
    input1 = "{}(){{{}}}"
    print(bool(closingParen(input1) == []))
