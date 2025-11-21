charList='a A b B'.split(' ')

for i in charList:
    char2Asc=ord(i)
    print(f'문자 {i}의 ascii값은 --> {char2Asc}')

for i in range(120):
    asc2Char=chr(i)
    print(f'ascii {i}의 문자는 --> {asc2Char}')
