class ItemToPurchase:
      def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

      def print_item_cost(self):
        return f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}"


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                item.item_quantity = item_to_purchase.item_quantity  # Only quantity updated
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def print_total(self):
        if len(self.cart_items) == 0:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("SHOPPING CART IS EMPTY")
        else:
            total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
            total_items = sum(item.item_quantity for item in self.cart_items)
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {total_items}")
            for item in self.cart_items:
                print(item.print_item_cost())
            print(f"Total: ${total_cost}")

def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("o - Output shopping cart")
        print("q - Quit")
        option = input("Choose an option: ").lower()

        if option == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(new_item)
            print(f"Added {item_quantity} of {item_name}.")

        elif option == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)

        elif option == 'c':
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            updated_item = ItemToPurchase(item_name, 0, new_quantity)
            cart.modify_item(updated_item)
            print(f"Updated {item_name} to {new_quantity} units.")

        elif option == 'o':
            cart.print_total()

        elif option == 'q':
            print("Thank you for using the shopping cart.")
            break

def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

if __name__ == "__main__":
    main()