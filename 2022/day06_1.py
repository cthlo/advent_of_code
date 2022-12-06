import fileinput

s = next(fileinput.input())
for i in range(len(s)):
    if len(set(s[i : i + 4])) == 4:
        print(i + 4)
        break
