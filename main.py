number = int(input('WRITE NUMBER: '))
float_number = 1.23
float_number2 = 23.563
text_str = 'Hello world'
text_str2 = 'program'
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

print("NUMBERS: ", number,"/ ", float_number,"/ ",float_number2,'/ ' , number_list[2],"/ ", tuple_list[0])
print("TEXT: ", text_str,"/ ",text_str2,'/ ', list(set_list)[0], "/ ", vocabulary['1'])
print("CLASSES: ", type(number), type(float_number),type(float_number2), type(text_str),type(text_str2), type(bool_variable),
      type(set_list), type(tuple_list), type(number_list), type(vocabulary))
