import fileinput

count = 0
for line in fileinput.input():
    policy, password = line.split(": ")
    times, letter = policy.split()
    lowest, highest = [int(t) for t in times.split("-")]

    if lowest <= password.count(letter) <= highest:
        count += 1

print(count)
