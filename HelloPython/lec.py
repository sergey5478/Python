path = 'text123.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_poc = data.index(' ')
    numbers.append(int(data[:space_poc]))
    data = data[space_poc + 1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))
    
print(out)
