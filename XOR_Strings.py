def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:  # Fix the equality check
            res += '0'  # Fix assignment to concatenation
        else:
            res += '1'  # Fix assignment to concatenation

    return res

s = input()
t = input()
print(strings_xor(s, t))
