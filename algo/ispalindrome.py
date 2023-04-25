#sentce except non letter signs and Uppercase conver to under case
import re
def ispalindrome(sentence):
    new = re.sub(r'[\W_]', '', sentence).lower()
    return new == new[::-1]


if __name__ == "__main__":
    sentence = input()
    print("Your word is: ", ispalindrome(sentence))
