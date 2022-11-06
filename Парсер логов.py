# Парсер логов 
path = "E:\log.log"# Здесь вводится путь к файлу с логами
path_ans = "E:\\ans_parser.txt" # Здесь вводится путь к файлу с логами
word = input() # Здесь должно быть введено слово
with open(path, 'r') as f:
    data = f.readlines()
print(data[0])
print(data[1])
print(data[2])
ans = []
for log in data:
    if word in log:
        ans.append(log)
with open(path_ans, 'w') as f:
    for line in ans:
        print(line)
        f.write("%s\n" % line)

