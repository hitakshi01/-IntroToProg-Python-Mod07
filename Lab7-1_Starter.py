# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# <Hitakshi>,<08.21.2020>, Created function in script to dump and load the data
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []


# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "wb")
    pickle.dump(list_of_data, objFile)
    objFile.close()


def read_data_from_file(file_name):
    objFile = open(file_name, "rb")
    data = pickle.load(objFile)
    objFile.close()
    return data

    # Presentation ------------------------------------ #


intID = input("Enter ID:   ")
StrName = input("Enter Name:  ")
lstCustomer = [intID, StrName]
save_data_to_file(strFileName, lstCustomer)
print(read_data_from_file(strFileName))
