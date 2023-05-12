def lengthOfLongestSubstring(s: str):
    if len(s) <= 1:
        return len(s)
    d = {}
    max_s = 0
    for i in s:
        if i in d.keys():
            max_s = max(max_s, len(d))
            for key in list(d.keys()):
                d.pop(key)
                if key == i:
                    break
        d[i] = 1
    max_s = max(max_s, len(d))
    return max_s


if __name__ == "__main__":
    s = input()
    print(lengthOfLongestSubstring(s))
