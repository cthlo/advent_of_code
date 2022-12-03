import fileinput

prios = {chr(i + 97): i + 1 for i in range(26)} | {
    chr(i + 65): i + 27 for i in range(26)
}

print(
    sum(
        prios[
            set(line[: len(line) // 2]).intersection(set(line[len(line) // 2 :])).pop()
        ]
        for line in fileinput.input()
    )
)
