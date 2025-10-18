# Prakash Fruit Shop Register
# This program will help manage fruit sales for customers in a simple way.

# Function to display the list of fruits with their prices per kilogram
def show_menu(fruit_list):
    print("Fruit List (per kg):")
    for fruit in fruit_list:
        print(fruit.capitalize(), "-", "$" + str(fruit_list[fruit]))
    print()  # Adds a blank line for better readability

# Function to get user input and make sure it is not blank
def get_input(msg):
    inp = input(msg).strip()
    while inp == "":
        print("Input cannot be blank.")
        inp = input(msg).strip()
    return inp

# Function to get a number greater than zero (used for weight or payment)
def get_positive_number(msg):
    while True:
        try:
            num = float(input(msg))
            if num > 0:
                return num
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to process the customer's payment, either by cash or card
def handle_payment(amount):
    print("You need to pay: $", round(amount, 2))
    method = get_input("Cash or card? ").lower()
    if method == "card":
        print("Payment received by card.")
        print("Thank you for shopping at Prakash Fruit Shop.")
    elif method == "cash":
        cash = get_positive_number("How much cash? $")
        if cash >= amount:
            print("Change: $", round(cash - amount, 2))
            print("Payment complete. Thank you for shopping at Prakash Fruit Shop.")
        else:
            left = amount - cash
            print("Remaining amount to pay: $", round(left, 2))
            again = get_input("Pay the rest by cash or card? ").lower()
            if again == "card":
                print("Remaining balance paid by card.")
                print("Thank you for shopping at Prakash Fruit Shop.")
            elif again == "cash":
                more = get_positive_number("Enter additional cash: $")
                if more >= left:
                    print("Payment complete. Thank you for shopping at Prakash Fruit Shop.")
                else:
                    print("Still not enough. Payment cancelled.")
            else:
                print("Invalid payment method. Transaction cancelled.")
    else:
        print("Invalid payment method. Transaction cancelled.")

# Main program to manage the shop process
def main():
    fruits = {
        "apple": 5.0,
        "banana": 3.0,
        "kiwi": 6.0,
        "watermelon": 7.0,
        "orange": 4.5,
        "mango": 8.0
    }

    print("Welcome to Prakash's Fruit Shop")
    print("================================")

    while True:
        print("\nNew customer...\n")
        show_menu(fruits)
        cart = []  # List to store what the customer buys

        while True:
            fruit = get_input("Enter fruit name (or 'done' to finish): ").lower()
            if fruit == "done":
                break
            if fruit not in fruits:
                print("Sorry, we don't sell that fruit.")
                continue
            weight = get_positive_number(f"Enter weight of {fruit} in kg: ")
            cost = fruits[fruit] * weight
            cart.append((fruit, weight, cost))
            print(f"Added {weight}kg {fruit} - ${round(cost, 2)}")

        if len(cart) == 0:
            print("No items purchased.")
        else:
            total = 0
            print("\nReceipt:")
            for item in cart:
                print(f"{item[0].capitalize()} ({item[1]}kg) - ${round(item[2], 2)}")
                total += item[2]
            print("Total: $", round(total, 2))
            handle_payment(total)

        nxt = get_input("Next customer? (yes/no): ").lower()
        if nxt != "yes":
            print("Shop is now closed. Goodbye!")
            break

# Start the program
if __name__ == "__main__":
    main()
