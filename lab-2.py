main_list = [1, 23,74,27,95,25,76,74,235,34, "potato", "tomato", "apple", "orange", "onion", "kiwi", "pepsi", "cola", "fanta", "sprite"]
int_list = []
str_list = []
kratni_dwom = []
upp_words = []

sort_list = []
for i in main_list:
    if type(i) == int:
         int_list.append(i)
    elif type(i) == str:
         str_list.append(i)

int_list.sort()
str_list.sort()
sort_list = list(int_list) + list(str_list)

for i in int_list:
    if i % 2 == 0:
        kratni_dwom.append(i)

for i in str_list:
    upp_words.append(i.upper())

print("ГОЛОВНИЙ СПИСОК: ", main_list )
print("СОРТОВАНИЙ СПИСОК: ", sort_list)
print("КРАТНІ ДВОМ:  ", kratni_dwom)
print("СЛОВА В ВЕРХНЬОМУ РЕГІСТРІ: ", upp_words)
