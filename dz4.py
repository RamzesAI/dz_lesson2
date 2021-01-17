user_str = input(('Напиши строку из нескольких слов, разделяя их пробелами: \n>>>'))
for num, element in enumerate(user_str.split()):
    print((num + 1), element[:10])
