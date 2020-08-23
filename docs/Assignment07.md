Hitakshi Verma

August 21, 2020

Foundations of Programming: Python

Assignment 07

gitHubURL:
                                                
  ### Create a script using exception error handling and pickling

**Introduction:**

Under the guidance of my professor, Randal Root, I have learnt how to create scripts using custom functions, files and structured error handling. As a part of my assignment, I am going to share my knowledge on structured error handling and pickling; sharing some resource links with you folks for your better understanding about these topics.
Also, I am going to create a script that demonstrates python’s structural error handling and pickling concept.
I believe you all are ready and curious to know these concepts. So, let’s get started.

**Pickling and Unpickling in Python:**

Python’s pickle module is used for serializing and de-serializing python object structures. The process to converts any kind of python objects (list, dict, etc.) into byte streams (0s and 1s) is called pickling or serialization or flattening or marshalling. We can convert the byte stream (generated through pickling) back into python objects by a process called as unpickling.
In real world scenarios, “pickling” is needed when we have to transfer data from one server/system to another and then store it in a file or database.
It is advisable not to “unpickle” data received from an untrusted source as they may pose security threat. Pickle module has no way of knowing or raising alarm while pickling malicious data.
To pickle the data, first we have to import the “pickle” module in our python script.
Pickle module has two main functions: dump and load. The first one is dump, which dumps an object to a file object and the second one is load, which loads an object from a file object.
To understand the basics of picking and unpickling in more detail. Please navigate to the following links provided below as these links not only gives you basic understanding but also helps you to get familiar with other useful functions and exception handling presented in pickle module.

•	https://www.tutorialspoint.com/python-pickling

•	https://thepythonguru.com/pickling-objects-in-python/ 

•	https://docs.python.org/3/library/pickle.html

I am also sharing a link with you if you are interested from “software security perspective. 

•	https://www.synopsys.com/blogs/software-security/python-pickling/

**Working on LAB 7-1:**

In this lab, I am going to create a function that saves data to a binary file using dump() function and loads object from file using load() function. For this, I am using my professor, Randal Root’s starter file.
```# ------------------------------------------------- #
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
```

![Results of Figure1](https://github.com/hitakshi01/-IntroToProg-Python-Mod07/blob/master/docs/Figure1.png "Results of Figure 1")

![Results of Figure2](https://github.com/hitakshi01/-IntroToProg-Python-Mod07/blob/master/docs/Figure2.png "Results of Figure 2")

###### *Figure1 and 2 demonstrates the data saved into binary file using dump and loaded from file using load function*

**Structured Error Handling:**

Generally, there are two types of errors in programming- syntax errors and exceptions. Here we are more interested in knowing exceptions and how we handle exceptions.
When a statement or expression is syntactically correct but an error is caused during its execution, then it is called as “exception”. When that error occurs, Python details what type of exception error was encountered. Exceptions are convenient in many ways for handling errors and special condition in a program. When we think that we have a code which can produce an error then we can use exception handling. We can raise an exception in your own program by using the “raise” exception statement.
Raising an exception breaks current code execution and returns the exception back until it is handled. We can trap errors using try- catch block when we think there is some condition that might cause an error and puts that condition in exception block.

"Exception" is a built-in python class used to hold information about an error. Python automatically creates an Exception object when an error occurs. The Exception object automatically fills with information about the error that caused the exception.

For more details about structural handling, folks, you can try these links which helps you to learn how to do exception handling in more details. 
•	https://realpython.com/python-exceptions/

•	https://www.programiz.com/python-programming/exception-handling




