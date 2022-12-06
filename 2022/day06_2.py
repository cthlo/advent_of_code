import fileinput

s = next(fileinput.input())
for i in range(len(s)):
    if len(set(s[i : i + 14])) == 14:
        print(i + 14)
        break
