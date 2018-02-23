import zipfile


file = zipfile.ZipFile('./zadanie_1_words.zip', 'r')

letters = dict()

for name in file.namelist():
    data = file.read(name).decode('UTF-8')

    for char in data:
        lower = char.lower()
        if lower in letters.keys():
            letters[lower] += 1
        else:
            letters[lower] = 1

result = ''
for item in sorted(letters.items()):
    result += (item[0] + str(item[1]))

print(result)
