# ------------------------------------------------- #
# Title: Lab7-1
# Description: This script stores and reads data to and from binary file using pickling and exception handling
# ChangeLog: (Who, When, What)
# <Hitakshi>,<08.21.2020>, Created script to write and read to and from binary file using dump and load function
# <Hitakshi>,<08.22.2020>, Created custom exception classes
# <Hitakshi>,<08.23.2020>, Added exception handling
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
class SaveException(Exception): # Custom exception class created for save operation
    def __str__(self):
        return 'There was a problem in saving data to file'

class ReadException(Exception): # Custom exception class created for read operation
    def __str__(self):
        return 'There was a problem in reading data from file'

def save_data_to_file(file_name, list_of_data):
    try:
        objFile = open(file_name, "wb")
        pickle.dump(list_of_data, objFile) # data is saved in binary file using dump() function
        objFile.close()
    except Exception as e: # catch all generic exception
        raise SaveException(e) # raise custom exception for user readability

def read_data_from_file(file_name):
    try:
        objFile = open(file_name, "rb")
        data = pickle.load(objFile) # data is read from the binary file
        objFile.close()
        return data
    except Exception as e: # catch all generic exception
        raise ReadException(e) # raise custom exception for user readability

# Presentation ------------------------------------ #

try:
    intID = input("Enter ID:   ")
    if not intID.isdigit():
        raise Exception("ID can only be numbers!") # Exception raised when user enters alphanumeric character in ID
    strName = input("Enter Name:  ")
    if not strName.isalpha():
        raise Exception("Name can only be alphabets!")# Exception raised when user is not entering characters in Name
    lstCustomer = [intID, strName] #Adding name and id to list
    save_data_to_file(strFileName, lstCustomer) # saving data to binary file using function
    print(read_data_from_file(strFileName)) # reading data from binary file using function
except Exception as e1: # raised and generic exception are caught by the exception base class
    print("There was an error!!")
    print(e1) # prints exception object
except SaveException as e2: #catches raised exception during "save_data_to_file"
    print(e2.__str__())
    print(e2)
except ReadException as e3: #catches raised exception during "read_data_from_file"
    print(e3.__str__())
    print(e3)