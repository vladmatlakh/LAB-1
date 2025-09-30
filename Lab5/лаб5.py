
# 1. NumPy
try:
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print("NumPy приклад: середнє значення =", np.mean(arr))
except Exception as e:
    print("Помилка в NumPy:", e)

# 2. Pandas
try:
    import pandas as pd
    data = {"Ім'я": ["Аня", "Олег", "Іра"], "Вік": [20, 22, 19]}
    df = pd.DataFrame(data)
    print("\nPandas приклад:\n", df)
except Exception as e:
    print("Помилка в Pandas:", e)

# 3. Matplotlib
try:
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
    plt.title("Matplotlib приклад")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
except Exception as e:
    print("Помилка в Matplotlib:", e)

# 4. Seaborn
try:
    import seaborn as sns
    sns.set(style="darkgrid")
    tips = sns.load_dataset("tips")   # приклад вбудованого датасету
    sns.histplot(tips["total_bill"], bins=20, kde=True)
    plt.title("Seaborn приклад (графік рахунків)")
    plt.show()
except Exception as e:
    print("Помилка в Seaborn:", e)

# 5. PrettyTable
try:
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["Місто", "Населення"]
    table.add_row(["Київ", "2.9 млн"])
    table.add_row(["Львів", "0.7 млн"])
    table.add_row(["Одеса", "1.0 млн"])
    print("\nPrettyTable приклад:\n", table)
except Exception as e:
    print("Помилка в PrettyTable:", e)