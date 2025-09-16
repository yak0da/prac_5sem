while n := input():     # внутри while нельзя сразу приводить к int, так как при вводе пустой строки будет ошибка
    if n == '13':
        print("ALARM")
        exit()
    if int(n) % 2 == 0:
        print(n)
print("CONGRATS")