number = int(input('WRITE NUMBER: '))
float_number = 1.23
text_str = 'Hello world'
bool_variable = bool
number_list = [1,2,3,4,5,6]
tuple_list = (1,2,3,4,5,6)
text = "hello world"
set_list = set(text)
vocabulary = {'1': 'computer', '2': 'programming'}

if number <= 5:
    bool_variable = True
    print(bool_variable)
elif number >5:
    bool_variable = False
    print(bool_variable)

print("NUMBERS: ", number,"/ ", float_number,"/ ", number_list[2],"/ ", tuple_list[0])
print("TEXT: ", text_str,"/ ", list(set_list)[0], "/ ", vocabulary['1'])
print("CLASSES: ", type(number), type(float_number), type(text_str), type(bool_variable),
      type(set_list), type(tuple_list), type(number_list), type(vocabulary))
