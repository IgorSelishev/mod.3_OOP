import os

# def walk_desc(path = None):
#     start_path = path if path is not None else os.getcwd()

#     for root, dirs, files in os.walk(start_path):
#         print("Текущая директория", root)
#         print("___")

#         if dirs:
#             print("Список папок", dirs)
#         else:
#             print("Папок нет")
#         print("___")

#         if files:
#             print("Список фалов", files)
#         else:
#             print("Фалов нет")
#         print("___")

#         if files and dirs:
#             print("Все пути:")
#         for f in files:
#             print("Файл ", os.path.join(root, f))
#         for d in dirs:
#             print("Папка", os.path.join(root, d))
#         print("===")

# walk_desc()

# f = open('text.txt', 'w', encoding='utf8')

# f.write('This is a test string\n')
# f.write('This is a test string\n')

# f.close()

# f = open('text.txt', 'r', encoding='utf8')
# print(f.read())
# f.close()

# f = open('text.txt', 'a', encoding='utf8')
# sequence = ['other string\n', '123\n', 'test test\n']
# f.writelines(sequence)
# f.close()

# f = open('text.txt', 'r', encoding='utf8')
# print(f.readlines())
# f.close

f = open('text.txt', 'r', encoding='utf8')
print(f.readline())
print(f.read(4))
print(f.readline())

f.close()