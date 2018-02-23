filename = './triangle.txt'

with open(filename, "r") as triangle:
    lines = []
    for line in triangle:
        lines.append(line.lstrip())

result = []

for line in lines:
    result.append([int(num) for num in line.split(' ')])

for line in range(len(result) - 1):
    last_line = result[-1]
    second_to_last_line = result[-2]

    for i in range(len(second_to_last_line)):
        second_to_last_line[i] += max(last_line[i], last_line[i + 1])
    result.pop(-1)
    result[-1] = second_to_last_line

print(result[0][0])
