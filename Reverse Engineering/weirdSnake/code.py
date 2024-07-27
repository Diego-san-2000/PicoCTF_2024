input_list = [4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0, 57, 32, 108, 23, 48, 4, 9, 70, 7, 110, 36, 8, 108, 7, 49, 10, 4, 86, 43, 104, 44, 91, 7, 18, 106, 124, 89, 78]
key_str = 't_Jo3'
key_list = [ord(char) for char in key_str]

while len(key_list) < len(input_list): 
    key_list.extend(key_list)

result = [a ^ b for a, b in zip(input_list, key_list)]
print(''.join(map(chr, result)))