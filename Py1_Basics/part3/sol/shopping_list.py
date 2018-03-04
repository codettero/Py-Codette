# Shopping List
# Demonstrates list methods

items = []
choice = None
while choice != "0":
    print(
    """
    High Scores
    0 - Exit
    1 - Show Items
    2 - Add an Item
    3 - Delete an Item
    4 - Sort Items
    """
    )
    
    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")
    # list the items to buy
    elif choice == "1":
        print("Shopping list items")
        for item in items:
            print(item)
    # add a score
    elif choice == "2":
        item = input("What other item do you have to buy?: ")
        items.append(item)
    # remove a score
    elif choice == "3":
        item = int(input("Remove which item?: "))
        if item in items:
            items.remove(item)
        else:
            print(item, "isn't in the shopping list.")
    # sort items
    elif choice == "4":
        items.sort(reverse=True)
    # some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")
