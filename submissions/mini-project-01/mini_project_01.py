import sys

grocery = []

def main():
    error = 0
    view = 0
    while error < 10:
        print("Options:",
            "1. Add item to the shopping list",
            "2. View shopping list",
            "3. Remove item from the shopping list",
            "4. Quit", sep = '\n')
        option = input("Enter the number of your choice: ")

        if option == '1':
            add_to_list("Enter the item you want to add: ")
        elif option == '2':
            view_list("Your shopping list: ")
            view += 1
        elif option == '3':
            remove_from_list("Enter the item you want to remove: ")
        elif option == '4':
            if view > 0:
                print("Goodbye!")
            else:
                view_list("Your shopping list: ")
                print("Goodbye!")
                break
        else:
            print("Invalid Input")
            error += 1
        #print newline before another loop
        print("")

    #outside the loop
    if error < 10:
        sys.exit(0)
    else:
        print("Too many errors")
        sys.exit(1)

def add_to_list(prompt):
    item = input(prompt).strip().capitalize()
    if item not in grocery:
        grocery.append(item)
    else:
        print("Item already in list.")
        return 0

def view_list(prompt):
    grocery.sort()
    print(prompt)
    if len(grocery) > 0:
        for item in grocery:
            print(item)
    else:
        print("The list is empty.")

def remove_from_list(prompt):
    item = input(prompt).strip().capitalize()
    if item in grocery:
        grocery.remove(item)
    else:
        print(f"{item} not in list.")
        view_list("Your shopping list: ")

if __name__ == "__main__":
    main()
