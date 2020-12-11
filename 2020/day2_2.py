import fileinput

count = 0
for line in fileinput.input():
    policy, password = line.split(": ")
    times, letter = policy.split()
    i, j = [int(t) for t in times.split("-")]

    try:
        a = int(password[i - 1] == letter)
    except IndexError:
        a = 0
    try:
        b = int(password[j - 1] == letter)
    except IndexError:
        b = 0

    count += a ^ b

print(count)
