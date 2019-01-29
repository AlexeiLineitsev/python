# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# igpkjgkj
# ;lkjhpokhnj
# jkljhgoln

import os

# for i in range(1,9):
#     dir_path = os.path.join(os.getcwd(), 'Dir_{}'.format(i))
#     try:
#         os.mkdir(dir_path)
#     except FileExistsError:
#         print('Такая директория уже существует')


# for i in range(1,9):
#     dir_path = os.path.join(os.getcwd(), 'Dir_{}'.format(i))
#     try:
#         os.removedirs(dir_path)
#     except FileNotFoundError:
#         print('Нет такой директории')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# current_dir_path = os.path.join(os.getcwd())
#
# list_files_and_dir = os.listdir(current_dir_path)
#
#
# for i in list_files_and_dir:
#     dir_path = os.path.join(current_dir_path,i)
#     if os.path.isdir(dir_path):
#         print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
