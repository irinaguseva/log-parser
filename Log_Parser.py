# Парсер логов

# Блок 1
path = input() # Здесь вводится путь к файлу с логами, например, E:\\log.log
path_ans = "E:\\ans_parser.txt" # Здесь находится путь к файлу с ответом

# Блок 2
word = input() # Здесь должно быть введено слово
with open(path, 'r') as f:
    data = f.readlines()
ans = []
for log in data:
    if word in log:
        ans.append(log)

# Блок 3
with open(path_ans, 'w') as f:
    for line in ans:
        print(line)
        f.write("%s\n" % line)

        
