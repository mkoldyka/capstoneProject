import os

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        '''Initialize the shoe object'''
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        '''Get the total cost of the shoe'''
        cost = self.cost * self.quantity
        return cost

    def get_quantity(self):
        '''Get the quantity of the shoe'''
        return self.quantity

    def __str__(self):
        '''Return the string representation of the shoe object'''
        return f"{self.country:<20}{self.code:<10}{self.product:<20}{self.cost:<10}{self.quantity:<10}"


shoe_list = [] # list to store the shoe objects

def print_header(withCost=False):
    '''Print the header of the table'''
    if withCost:
        print(f"{'Country':<20}{'Code':<10}{'Product':<20}{'Cost':<10}{'Quantity':<10}{'Total Cost':<10}")
    else:
        print(f"{'Country':<20}{'Code':<10}{'Product':<20}{'Cost':<10}{'Quantity':<10}")
    
def clear_screen():
    '''Clear the screen'''
    os.system("cls") # clear the screen

def read_shoes_data():
    '''Read the shoes data from the file'''
    if len(shoe_list) > 0: # if the shoe list is not empty
        shoe_list.clear() # clear the shoe list
    try:
        with open("inventory.txt", "r") as file:
            file.readline() # skip the first line
            for line in file:  # go through each line in the file
                line = line.strip().split(",") # remove the new line character and split the line into a list
                shoe = Shoe(line[0], line[1], line[2], line[3], line[4])  # create a shoe object
                shoe_list.append(shoe) # append the shoe object into the shoe list
    except FileNotFoundError: # if the file is not found
        print("File not found") # print the message
    

def capture_shoes():
    '''Capture the shoes data from the user'''
    clear_screen()
    # get the data from the user
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = input("Enter the cost: ")
    quantity = input("Enter the quantity: ")
    shoe = Shoe(country, code, product, cost, quantity) # create a shoe object
    shoe_list.append(shoe) # append the shoe object into the shoe list
    

def view_all():
    '''View all the shoes'''
    clear_screen()
    print_header()
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    '''Restock the shoe'''
    clear_screen()
    lowest_quantity_shoe = shoe_list[0] # set the lowest quantity shoe to the first shoe in the list
    for shoe in shoe_list: # go through each shoe
        if shoe.get_quantity() < lowest_quantity_shoe.get_quantity(): # if the quantity of the shoe is less than the quantity of the lowest quantity shoe
            lowest_quantity_shoe = shoe # set the lowest quantity shoe to the current shoe

    print(f"The shoe with the lowest quantity is: {lowest_quantity_shoe}") # print the shoe with the lowest quantity
    answer = input("Do you want to add this quantity of shoes? (y/n): ") # ask the user if they want to add the quantity of shoes
    if answer == "y": # if the user wants to add the quantity of shoes
        for shoe in shoe_list: # go through each shoe
            if shoe.get_quantity() == lowest_quantity_shoe.get_quantity(): # if the quantity of the shoe is equal to the quantity of the lowest quantity shoe
                quantity_to_add = int(input("Enter the quantity to add: ")) # get the quantity to add from the user
                shoe.quantity += quantity_to_add # add the quantity
                print("The quantity has been updated.") # print the message
                break
    else:
        print("The quantity has not been updated.") # if the user does not want to add the quantity of shoes print this message
    
    with open("inventory.txt", "w") as file: # open the file in write mode
        file.write("Country,Code,Product,Cost,Quantity") # write the header
        for shoe in shoe_list: # go through each shoe
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n") # write the data
    
        

def search_shoe():
    '''Search for a shoe using the shoe code'''
    clear_screen()
    code = input("Enter the shoe code: ") # get the shoe code from the user
    for shoe in shoe_list: # go through each shoe
        if shoe.code == code: # if the shoe code is equal to the code entered by the user
            print(shoe) # print the shoe
            break
    else: # if the shoe code is not found to the code entered by the user
        print("Shoe not found.")

def value_per_item():
    '''Print the value per item'''
    clear_screen()
    print_header(True) # print the header with the total cost
    for shoe in shoe_list: # go through each shoe
        print(f"{shoe.country:<20}{shoe.code:<10}{shoe.product:<20}{shoe.cost:<10}{shoe.quantity:<10}{shoe.get_cost():<10}")


def highest_qty():
    '''Print the shoe with the highest quantity'''
    clear_screen()
    highest_quantity_shoe = shoe_list[0] # set the highest quantity shoe to the first shoe in the list
    for shoe in shoe_list: # go through each shoe
        if shoe.get_quantity() > highest_quantity_shoe.get_quantity(): # if the quantity of the shoe is greater than the quantity of the highest quantity shoe
            highest_quantity_shoe = shoe # set the highest quantity shoe to the current shoe
    print(f"The shoe with the highest quantity is:")
    print_header()
    print(f"{highest_quantity_shoe}")
    


print("=====================================")
print("Welcome to the shoe inventory system")
print("=====================================")

while True:
    print()
    print("Main Menu:")
    print("1. Read shoes data")
    print("2. View all shoes")
    print("3. Capture new shoe")
    print("4. Re-stock")
    print("5. Search for a shoe")
    print("6. Value per item")
    print("7. Highest quantity")
    print("8. Exit")
    option = input("Enter your option: ")
    if option == "1":
        read_shoes_data()
    if option == "2":
        view_all()
    elif option == "3":
        capture_shoes()
    elif option == "4":
        re_stock()
    elif option == "5":
        search_shoe()
    elif option == "6":
        value_per_item()
    elif option == "7":
        highest_qty()
    elif option == "8":
        break
    else:
        print("Invalid option")