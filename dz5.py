my_list = [7, 5, 3, 3, 2]

new_item = int(input(('Add new element')))

check_item = (new_item) in my_list

if check_item == False:
    my_list.append(new_item)
    print(sorted(my_list, reverse=True))

if check_item == True:
    number_of_element = (my_list.index(new_item))
    some_of_elements = my_list.count(new_item)
    my_list.insert(number_of_element + some_of_elements, new_item)
    print(my_list)


