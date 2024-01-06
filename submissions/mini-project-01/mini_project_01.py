from sys import exit

grocery = []

def main():
    error = 0
    view = False
    while error < 10:
        print("Options:",
            "1. Add item to the shopping list",
            "2. View shopping list",
            "3. Remove item from the shopping list",
            "4. Quit", sep = '\n')
        option = input("Enter the number of your choice: ")

        if option == '1':
            add_to_list("Enter the item you want to add: ")
            view = False
        elif option == '2':
            view_list("Your shopping list: ")
            view = True
        elif option == '3':
            remove_from_list("Enter the item you want to remove: ")
            view = False
        elif option == '4':
            if view:
                print("Goodbye!\n")
                break
            else:
                view_list("Your shopping list: ")
                print("Goodbye!\n")
                break
        else:
            print("Invalid Input")
            error += 1
        #print newline before another loop
        print("")

    #outside the loop
    if error < 10:
        exit(0)
    else:
        print("Too many errors")
        exit(1)

def add_to_list(prompt):
    item = input(prompt).strip().capitalize()
    if item not in grocery:
        grocery.append(item)
    else:
        print("Item already in list.")

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
