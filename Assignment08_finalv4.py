# ------------------------------------------------------------------------ #
# Title: Assignment 08: Working with classes
# Description: Script will ask for user input of product name
#              and price, create a product object and use the setter property to determine
#              whether the product name and price are appropriately entered as letters and numbers
#              respectively. Reading and writing and menu choices are similar to Assignment06
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Hedy Khalatbari,08.21.2021,Modified code to complete assignment 8
#                 08.24.2021, Modifed code for deleting an item as there was a logic error
#                 08.25.2021 Modified code to instantiate a product object per row when loading f
#                            from file
# --------------------------------------------------------------------------------- #
import os  # imports os module

# Data, start -------------------------------------------------------------------- #
strFileName = 'products.txt'  # name of the data file
file = None                   # object that represents a file
lstOfProductObjects = []      # list of product objects
strChoice = ""                # Captures the user option selection
strProduct = ""               # Captures the product name
objProduct = ""               # Captures a newly created object from the Product class
floatPrice = ""               # Captures the product price
status = ""                   # Captures a message to return & print for user feedback

class Product():
    """Stores data about a product:

    properties:
        product_name: (string) with the product's name
        product_price: (float) with the product's standard price
    methods:
        __str__: (string) product_info (name and price)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Hedy Khalatbari,08.21.2021,Modified code to complete assignment 8
    """

    # define constructor, getters and setters
    # define __str__ that will return product_info (product name & price)

    def __init__(self, product_name='', product_price=''):
        self.__product_name = product_name
        self.__product_price = product_price

    def __str__(self):
        product_price = str(self.__product_price)
        product_info = self.__product_name + ', ' + product_price
        return product_info  # a string with product name and price; used to save product object to list

    # getter and setter for product_name
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:   # checks that it is not numeric
            value = value.strip().lower()     # lower case & strip
            self.__product_name = value       # sets it if condition fulfilled
        # otherwise, the product_name remains as '' (i.e., an empty string)

    # getter and setter for product_price
    @property
    def product_price(self):
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        value = value.strip()                    # strip
        if str(value).isnumeric() == True:       # checks if numeric
            self.__product_price = float(value)  # sets it as a float
        # otherwise, the product_price remains as '' (i.e., an empty string)
        
# Data, end -------------------------------------------------------------------- #


# Processing, start  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        read_data_from_file(file_name): -> (a list of product objects)

        save_data_to_file(file_name, list_of_product_objects):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Hedy Khalatbari,08.21.2021,Modified code to complete assignment 8
    """

    # Code to process data to a file

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: string with name of file:
        :return: list of product objects, status
        """
        status = '' # added this here as was getting an error
        list_of_product_objects = []  # local variable, list of products names & prices
        if os.path.exists(file_name):  # used to check if the text file exists and run script if True
            file = open(file_name, "r")
            for line in file:
                if "," in line:  # added this condition as was getting an error when text file empty
                    product_name, product_price = line.split(',')
                    product_object = Product(product_name, product_price)  # create a product object
                    list_of_product_objects.append(str(product_object))
                    status = 'Data read from file.'
                else:
                    status = 'There is no data saved in the file.'
            file.close()
        else:
            status = 'File does not exist.'
        return list_of_product_objects, status

    @staticmethod
    def add_product_to_list(product, price, lstOfProductObjects):
        """ Adds user input data (product, price) to a list of dictionary rows

        :param product: (string) product we want to add:
        :param price: (string) price of product to add:
        :param lstOfProductObjects: (list) of dictionary rows
        :return:(list) of dictionary rows
        """
        new_product = Product(product, price)  # forms a class instance object
        lstOfProductObjects.append(str(new_product))   # save the properties of the instance object to list
        status = 'Product name and price were added to list.'
        return lstOfProductObjects, status

    @staticmethod
    def remove_data_from_list(product, lstOfProductObjects):
        """ Removes product from list of dictionaries

        :param product: (string) product we want to remove:
        :param lstOfProductObjects: (list) of products
        :return: (list) of products, success/failure of task
        """
        status = 'Product was not in list.'   # sets default status message
        product = product.strip().lower()     # product to be removed
        for row in lstOfProductObjects:       # in this function I did not treat rows as an object instance
            product_local, price = row.split(',')
            if product == product_local.strip():  # remove the user selected product
                lstOfProductObjects.remove(row)
                status = 'Product was removed.'  # changes status message to reflect that product was removed
        return lstOfProductObjects, status

    @staticmethod
    def write_data_to_file(file_name, lstOfProductObjects):
        """ Write data from a list of dictionary rows into a file

        :param file_name: (string) with name of file:
        :param lstOfProductObjects: (list) of dictionary rows:
        :return: status of task
        """
        status = 'No data to write to file.'
        file = open(file_name, "w")
        if lstOfProductObjects != []:    # check that list is not empty
            for row in lstOfProductObjects:
                file.write(row + '\n')
                status = 'Data was written to file.'
        file.close()
        return status



# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output products """

    @staticmethod
    def print_menu_products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options:
        1) Add a new product name & price
        2) Remove an existing product
        3) Save Data to File        
        4) Reload Data from File
        5) Show product name & price list
        6) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Products_in_list(lstOfProductObjects):
        """ Shows the current products

        :param lstOfProductObjects: list of product names and prices
        :return: nothing
        """
        print("**    Current product names and prices are:    **")
        if lstOfProductObjects != []:  # check whether list is empty
            for row in lstOfProductObjects:
                print(row.strip())
        else:
            print("There are no entries in the list.")
        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")
        print()  # Add an extra line for optimal presentation

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        choice = str(input(message))
        choice = choice.strip().lower()
        return choice

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product():
        """ Asks user to input new product

        :return: (strings) product name
        """
        productName = str(input("Enter product name: "))
        product_1 = Product()                   # instantiate an object from the class Product
        product_1.product_name = productName    # set the product name
        return product_1, product_1.product_name

    @staticmethod
    def input_new_price(product_object):
        """ Asks user to input new price

        :return: (strings) product price
        """
        productPrice = str(input("Enter product price: "))
        product_object.product_price = productPrice   # set the product price
        return product_object.product_price

    @staticmethod
    def input_product_to_remove():
        """ Asks user which product they would like to remove

        :return: (string) product
        """
        product = str(input("Enter product to remove: "))
        return product


# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, Load data from products.txt and print list of product names & prices
lstOfProductObjects, status = FileProcessor.read_data_from_file(strFileName)  # read file data into list
print(status)   # feedback to user regarding file contents
IO.print_current_Products_in_list(lstOfProductObjects)  # shows current products in the list

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show menu and ask user to choose a menu option
    IO.print_menu_products()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice == '1':  # Add a new product
        objProduct, strProduct = IO.input_new_product()
        if strProduct != '':     # checks that it is not numeric
            floatPrice = IO.input_new_price(objProduct)
            if floatPrice != '':    # checks to ensure value was assigned
                lstOfProductObjects, status = FileProcessor.add_product_to_list(strProduct, floatPrice,
                                                                                lstOfProductObjects)
                print(status)   # message to user
            else:
                print('Data rejected.Products names should only contain letters and '   # message to user
                      'product prices should only contain numbers.')
        else:
            print('Data rejected. Products names should only contain letters and '   # message to user
                  'product prices should only contain numbers.')
        IO.input_press_to_continue()
        continue  # to show the menu


    elif strChoice == '2':  # Remove an existing product
        strProduct = IO.input_product_to_remove()
        lstOfProductObjects, status = FileProcessor.remove_data_from_list(strProduct, lstOfProductObjects)
        print(status)
        IO.input_press_to_continue()
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            status = FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)
            print(status)
            IO.input_press_to_continue()
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstOfProductObjects, status = FileProcessor.read_data_from_file(strFileName)
            print(status)
            IO.print_current_Products_in_list(lstOfProductObjects)
            IO.input_press_to_continue()
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Show current data in the list of dictionary rows
        IO.print_current_Products_in_list(lstOfProductObjects)  # Show current data in the list of dictionary rows

    elif strChoice == '6':  # Exit Program
        print("Goodbye!")
        break  # and Exit

    else:
        print("Please choose from menu options")
