filename = './triangle.txt'

with open(filename, "r") as triangle:
    lines = []
    for line in triangle:
        lines.append([int(num) for num in line.strip().split(' ')])

for line in range(len(lines) - 1):
    last_line = lines[-1]
    second_to_last_line = lines[-2]

    for i in range(len(second_to_last_line)):
        second_to_last_line[i] += max(last_line[i], last_line[i + 1])
    lines.pop(-1)
    lines[-1] = second_to_last_line

print(lines[0][0])
