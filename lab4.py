def prise(price: float) -> str:
    return f"ціна: {price} грн."

def article_price(store: dict) -> dict:
    while True:
        article = input("Введіть товар( (-) - для закінчення):  ").strip().lower()
        if article == "-":
            break
        if article in store:
            print("Товар вже існує")
            continue
        price = float(input("Введіть ціну: "))
        store[article] = price
    return store

def article_presence (store: dict) -> dict:
    presence = {}
    for article in store:
        while True:
            presence_item = input(f'Чи є {article} у наявності? (так/ні): ').strip().lower()
            if presence_item == "ні":
                presence[article] = False
                break
            elif presence_item == "так":
                presence[article] = True
                break
            else:
                print("Можна вводити лише так/ні: ")
    return presence

def check_presence(article_to_check: list,presence: dict ) -> bool:
    all_article = True
    for article in article_to_check:
        if article not in presence or not presence[article]:
            print(f"{article} відсутній.")
            all_article = False
    return all_article

def total_price(order: list, store: dict) -> str:
    total = 0
    for i in order:
        total += store[i]
    return prise(total)

def calculate_order_price(presence: dict, store: dict):
    order = input("Введіть товари через кому: ").lower().split(",")
    order = [item.strip() for item in order]
    if check_presence(order, presence):
        ans = input("Купити чи переглянути ціну? (1/2): ").strip()
        if ans == "1":
            print(f"До сплати {total_price(order, store)}")
        elif ans == "2":
            print(f"Загальна {total_price(order, store)}")
        else:
            print("Некоректний ввід.")

def main():
    calculate_order_price(presence, store)

if __name__ == "__main__":
    store = {}
    article_price(store)
    presence = article_presence(store)
    main()
