group = {}

#Заповнення словника
while True:
    student_name = input("\nВведіть ім'я (або Enter для завершення): ")
    if student_name == "":
        break
    try:
        note = float(input("Введіть оцінку: "))
    except ValueError:
        print("Треба ввести число!")
        continue

    if student_name not in group:
        group[student_name] = []
    group[student_name].append(note)

#виведення середнього значення словника
all_values = []
for values in group.values():
    all_values.extend(values)
avenger = round(sum(all_values) / len(all_values), 2)

#розподіл студентів по оцінках
excellent={}
good_guys={}
laggards={}
did_not_pass={}

for student_name, notes in group.items():
    avg_note = sum(notes) / len(notes)
    if 12 >= avg_note >= 10:
        excellent[student_name] = avg_note
    elif 9 >= avg_note >= 7:
        good_guys[student_name] = avg_note
    elif 6 >= avg_note >= 4:
        laggards[student_name] = avg_note
    elif 3 >= avg_note >= 1:
        did_not_pass[student_name] = avg_note

if excellent:
    print("Відмінники", len(excellent), ": ")
    for key, value in excellent.items():
        print(f"{key}: {value}")

if good_guys:
    print("\nХорошисти", len(good_guys), ": ")
    for key, value in good_guys.items():
        print(f"{key}: {value}")

if laggards:
    print("\nВідстаючі", len(laggards), ": ")
    for key, value in laggards.items():
        print(f"{key}: {value}")

if did_not_pass:
    print("\nНе здали", len(did_not_pass), ": ")
    for key, value in did_not_pass.items():
        print(f"{key}: {value}")
print("Середній бал на групу: ", avenger)
