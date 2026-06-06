print("\n========== Currency Converter ==========\n")

# ---------------- DATA ---------------- #
currency = {
    "USD": 1,
    "INR": 83,
    "EUR": 0.95,
    "YEN": 150,
    "RIYAL": 3.75
}

history = []
pre_con = "None"
con_count = 0


# ---------------- MAIN MENU ---------------- #
def main_menu():
    print("\n===== MAIN MENU =====")
    print("1. Conversion")
    print("2. History")
    print("3. Exit")


# ---------------- CONVERSION MENU ---------------- #
def menu_con():
    print("\n===== CONVERSION MENU =====")
    print("1. Convert Currency")
    print("2. Add New Currency")
    print("3. Home")


# ---------------- HISTORY MENU ---------------- #
def menu_his():
    print("\n===== HISTORY MENU =====")
    print("1. View History")
    print("2. Clear History")
    print("3. Home")


# ---------------- PROGRAM START ---------------- #
while True:

    main_menu()

    choose_main = int(input("\nEnter choice: "))

    # =====================================================
    # CONVERSION SECTION
    # =====================================================
    if choose_main == 1:

        while True:

            menu_con()

            choose_con = int(input("\nEnter choice: "))

            # ---------------- CONVERT ---------------- #
            if choose_con == 1:

                while True:

                    print("\nAvailable currencies:\n")

                    for i, key in enumerate(currency.keys(), start=1):
                        print(i, ".", key)

                    print("\nPrevious Conversion :", pre_con)
                    print("Number of Conversions :", con_count)

                    from_c = input("\nFrom currency: ").upper()
                    to_c = input("To currency: ").upper()

                    amount = float(input("Amount: "))

                    if from_c in currency and to_c in currency:

                        # Convert to USD first
                        usd = amount / currency[from_c]

                        # Convert USD to target currency
                        convert = usd * currency[to_c]

                        value = f"{amount} {from_c} = {round(convert,2)} {to_c}"

                        print("\n", value)

                        with open("history.txt", "a") as file:
                        	file.write(value+"n")

                        pre_con = value

                        con_count += 1

                    else:
                        print("\nInvalid currency entered!")

                    print("\n1. Convert Again")
                    print("2. Back")

                    again = int(input("Enter choice: "))

                    if again == 1:
                        continue

                    elif again == 2:
                        break

                    else:
                        print("\nInvalid input!")

            # ---------------- ADD NEW CURRENCY ---------------- #
            elif choose_con == 2:

                print("\nAdd new currency")
                print("Example:")
                print("If 1 USD = 90 XYZ")
                print("Enter currency name = XYZ")
                print("Enter value = 90")

                new_currency = input("\nCurrency name: ").upper()

                new_value = float(input("Value: "))

                currency[new_currency] = new_value

                print("\nCurrency added successfully!")

            # ---------------- BACK TO HOME ---------------- #
            elif choose_con == 3:
                break

            else:
                print("\nEnter valid option!")

    # =====================================================
    # HISTORY SECTION
    # =====================================================
    elif choose_main == 2:

        while True:

            menu_his()

            choose_his = int(input("\nEnter choice: "))

            # ---------------- VIEW HISTORY ---------------- #
            if choose_his == 1:

                print("\n===== HISTORY =====")

                with open("history.txt", "r") as file:
                	print(file.read())
                

                back = input("\nType 'bye' to go back: ").lower()

                if back == "bye":
                    continue

            # ---------------- CLEAR HISTORY ---------------- #
            elif choose_his == 2:

                open("history.txt", "w").close()

                print("\nHistory cleared successfully!")

            # ---------------- HOME ---------------- #
            elif choose_his == 3:
                break

            else:
                print("\nInvalid choice!")

    # =====================================================
    # EXIT
    # =====================================================
    elif choose_main == 3:

        print("\nThank you for using Currency Converter!")
        break

    # =====================================================
    # INVALID INPUT
    # =====================================================
    else:
        print("\nPlease enter a valid option!")
