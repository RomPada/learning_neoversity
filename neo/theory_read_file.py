
# Ще є зручний спосіб читати файл порядково, по одному рядку за раз, для цього можна скористатися методом readline:

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()
