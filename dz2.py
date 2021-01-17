print('Тебе необходимо внести свои элементы в список')
new_list = []
n = int(input('Сколько элементов должно быть в списке?\n>> '))

while True:
    list_item = input('введи любой элемент списка (число, буква, слово...).\n>>')
    new_list.append(list_item)
    if len(new_list) == n:
        break

print('-------------------------------------------------------')
print('Список, который ты ввел: ', new_list)
j = 0
for i in range(int(len(new_list) / 2)):
    new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    j +=2
print(new_list)