string = 'результат операции: 42'

string_index = string.index(':')
sliced = string[string_index:]
clean = sliced.lstrip(': ')
res = int(clean) + 10
print(res)

string = 'результат операции: 514'
string_index = string.index(':')
sliced = string[string_index:]
clean = sliced.lstrip(': ')
res = int(clean) + 10
print(res)

string = 'результат работы программы: 9'
string_index = string.index(':')
sliced = string[string_index:]
clean = sliced.lstrip(': ')
res = int(clean) + 10
print(res)
