# File-Parse-IP-Address-WhiteList-Removal

## Cybersecurity Portfolio Activity: Update a file through a Python algorithm

### Introduction

The lab environment used is a Python notebook-based coding environment stored as an `.ipynb` file. 

An `.ipynb` file is a Python notebook file which contains the notebook code cells, markdown code cells, the execution results of the code cells and other internal settings in a specific format on the `Jupyter` environment.

Notebooks, such as this one, consist of two types of cells: 
1. **markdown** cells. 
2. **code** cells for writing and running Python code.

Markdown cells allow you to write plain text and format it in the markdown language. Markdown language is used for formatting plain text in text editors and code editors. For example, you can use markdown to make headers, bold or italicize words, format text as code, add hyperlinks, and more.

This notebook lists the steps needed to create an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list. If so, you should remove those IP addresses from the file containing the allow list.

## Scenario
You are a security professional working at a health care company. As part of your job, you're required to regularly update a file that identifies the employees who can access restricted content. The contents of the file are based on who is working with personal patient records. Employees are restricted access based on their IP address. 

There is an allow list for IP addresses permitted to sign into the restricted subnetwork. There's also a remove list that identifies which employees you must remove from this allow list.


Note that running the code in task 1-6 will produce an error because it will only contain the fragments of code that will need to be run all at once in a single code cell; you'll complete this with statement in the task after this.

For that reason, the code will be broken down into steps and placed together at the end to be run.


## Task 1: Open the file that contains the allow list

The code to use for this task is as follows:

```
import_file = “allow_list.txt”

with open(import_file, “r”) as file:
```

----

The variable `import_file` is created as a placeholder to hold the value of `"allow_list.txt"`, the filename of the file we want to open. 

A `with` statement starting with the keyword `with` is used to open a resource (in this case, the file we want to open) and guarantee that the resource will be closed whether the `with` code block completes successfully or not.

The `open()` function will do the action of opening the file and return the opened file as a file object.
    It takes two arguments in the following order, `import_file` for the file object to open and the string `"r"` to specify the file is opened for **reading**.


The variable `file` will be used to store contents of the `import_file` value to perform file based methods within the `with` statement code block.


 Note that running this code will produce an error because it will only contain the first line of the with statement; you'll complete this with statement in the task after this.


```python
# Assign import_file as filename we want to read the allow list from 

import_file = "allow_list.txt"

# Open the file that contains the allow list

with open(import_file, "r") as file:
```

## Task 2 - Read the file contents


Next, the `.read()` method will be invoked with the `file` object created with the `as` keyword to the save the contents of the IP address allow list as a string so that the data from the file can be read and used.


```python
# Read the file contents and convert to string to store in ip_addresses.

ip_addresses = file.read() 
```

## Task 3 - Convert the string into a list

The next step is to convert the data type of our ip_addresses placeholder from a string object into a list object. This is so we will be able to remove IP addresses from the allow list.





```python
# Convert the ip_addresses string object into a list object

ip_addresses = ip_addresses.split()
```

## Task 4 - Iterate through the remove list

A second list called `remove_list` contains all of the IP addresses that should be removed from the `ip_addresses` list. 

The next step is to set up the header of the `for` loop that will iterate through the `remove_list` using `element` as the loop variable. The keyword we need for this is `for` to signal the beginning the `for` loop and the `in` keyword to specify iterating through the sequence of elements in the `remove_list` list. 

I added an variable called `removal_counter` to count the number of removal operations done on the IP address allow list when the script is run.



```python
# Declare the remove_list list object with the IP addresses to be removed.

remove_list = ["192.168.116.187", "192.168.15.110", "192.168.39.246"]


# Iterate through each IP address in the IP address remove list 

removal_counter = 0

# for loop header 
for element in remove_list:

```

## Task 5 - Remove IP addresses that are on the remove list

After setting up the for loop header to traverse the `remove_list` list. The `for` loop body code was added:

- An `if` conditional statement is used to check if each `element` in the `remove_list` is in the `ip_addresses` list
    - If the IP address is found, we pass the `element` variable by into the `.remove()` method for the `ip_addresses` list.
    - A `print()` statement is used to show the value of IP address with a confirmation message it is removed as well as a statement to increment the `removal_counter` variable by one.
- An `else` conditional statement is used to print a message if a IP address in the `remove_list` is not found in the `allow_list`.

A final `print()` statement is used to print a string message with the total value of the `removal_counter` variable to show how many IP addreses were removed. the built-in function `str()` is used to convert the `removal_counter` datatype from integer to a string.



```python
  # check if loop variable is part of the ip_addresses list object and remove it
    if element in ip_addresses: 
        ip_addresses.remove(element)
        print("IP address: " + element + ", found and removed")
        removal_counter = removal_counter + 1

    # conditional statement if no IP addresses were found or removed during iteration.
    else:
        print("IP address: " + element + ", is not in the allow list.")

print("Total number of IP addresses removed: " + str(removal_counter))

```

## Task 6 - Update the import_file with the revised list of IP addresses.

The following code needed to update the `import_file` object is to update and convert ip_addresses from a list back into a string object using the new line operator string `\n` and the `.join()` with the `ip_addresses` passed into the `.join()` method as argument.

The new portion of code needed is to run the open() function on the
`import_file` with the second argument of `"w"` to specify that a write operation is going to be done on the `import_file` as the file object called `file`.

`file.write(ip_addresses)` is used take the new line formatted contents of the string `ip_addresses` and write it to the `import_file` file object.


The following print statements,

  `print("\nIP address allow list parsing complete.")`
   
  `print("-----------------\n" + ip_addresses + "\n-----------------")`


outputs the contents of
the `ip_addresses` as it will be shown in the `import_file`


```python
# Convert the ip_addresses list back into a string and printing the output 
# using the .join() method with each element separated by a new line 
ip_addresses = "\n".join(ip_addresses)

# Open the import_file to perform a write operation on it
with open(import_file, "w") as file:

    file.write(ip_addresses) 

    print("\nIP address allow list parsing complete.")

    print("-----------------\n" + ip_addresses + "\n-----------------")
```

## Task 7 - Entire code algorithm to compile 

To run the code, run the code cell or block with the filename or path matching in the same Jupyter Notebook environment or the development environment of your choice.

note: If no path is specified, it is assumed the text file is in the same directory as your python file that is executed with this script.


```python
#Assign import_file as filename or filename path we want to read the allow list from 

import_file = "allow_list.txt"

# Open the file that contains the allow list

with open(import_file, "r") as file:

    # Read the file contents and convert to string to store in ip_addresses.

    ip_addresses = file.read()

    # Convert the ip_addresses string object into a list object

    ip_addresses = ip_addresses.split() 


# Declare the remove_list list object with the IP addresses to be removed.

remove_list = ["192.168.116.187", "192.168.15.110", "192.168.39.246"]


# Iterate through each IP address in the IP address remove list 

removal_counter = 0

# for loop header 
for element in remove_list:

    # check if loop variable is part of the ip_addresses list object and remove it
    if element in ip_addresses: 
        ip_addresses.remove(element)
        print("IP address: " + element + ", found and removed")
        removal_counter = removal_counter + 1

    # conditional statement if no IP addresses were found or removed during iteration.
    else:
        print("IP address: " + element + ", is not in the allow list.")

print("Total number of IP addresses removed: " + str(removal_counter))


# Update the import_file with the revised list of IP addresses.

# Convert the ip_addresses list back into a string and printing the output 
# using the .join() method with each element separated by a new line 
ip_addresses = "\n".join(ip_addresses)


with open(import_file, "w") as file:

    file.write(ip_addresses) 

    print("\nIP address allowlist parsing complete.")

    print("-----------------\n" + ip_addresses + "\n-----------------")


```
#### Example Output

    IP address: 192.168.116.187, is not in the allow list.
    IP address: 192.168.15.110, is not in the allow list.
    IP address: 192.168.39.246, is not in the allow list.
    Total number of IP addresses removed: 0
    
    IP address allowlist parsing complete.
    -----------------
    192.168.218.160
    192.168.97.225
    192.168.145.158
    192.168.108.13
    192.168.60.153
    192.168.96.200
    192.168.247.153
    192.168.3.252
    -----------------


## Task 8 - Reset import_file contents 


Running this code cell resets the `"allow_list.txt"` file to its original contents in case the file has been changed and for demonstration purposes for further tinkering of the file parse script.



```python
import_file = """192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"""

# Writes `import_file` to the `"allow_list.txt"` file and displays confirmation output
with open("allow_list.txt", "w") as file:
    file.write(import_file)
    print("allow_list.txt file reset for demo purposes")
```

#### Example Output

    allow_list.txt file reset for demo purposes


## Conclusion

This script is an algorithm that checks whether an allow list text file contains any IP addresses identified on the remove list. If so, the IP addresses are removed from the file containing the allow list.

I went above and beyond and added the following:

    - Functionality to track the number of IP Address removals
    - Confirmation output to show script actions performed
    - Logic to show different output if no IP addresses entered in the remove list aren't present in the IP address allow list 

In Python, a `with` statement is often used with the `open()` function for file handling operations
The `open()` function takes two parameters, the name of the file you want to perform an action on and single letter string describing the action you want to perform on the specified file in the first argument.

- There are three inputs that can be entered as the second argument of the `open()` function:

    - The `"r"` string indicates a file is being opened for file reading actions.
    - The `"w"` string indicates a file is being opened for file writing actions.
    - The `"a"` string indicates a file is being opened for appending content to the end of a specified file.

- The `as` keyword is used to assign the file object returned by the `open()` function to a variable (e.g. file)

- The `.read()` method is used to read data from a file object

- The `.write()` method is used to write data to a file object.

