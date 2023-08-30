"""
This script is an algorithm that checks whether an allow list text file contains 
any IP addresses identified on the remove list. If so, the IP addresses are removed from the file containing the allow list.

I went above and beyond and added the following:

    - Functionality to track the number of removals done on the file
    - Output to show script actions performed
    - Logic to show output if no IP addresses entered in the remove list aren't present in the IP address allow list 
    - Optional functionality that can be removed to allow the script to be demoed  


This script was created as part of course work for the Google Cybersecurity Professional Coursera Certificate for a example scenario. 

Example Scenario:
-------------------------

You are a security professional working at a health care company. 
As part of your job, you're required to regularly update a file that identifies
the employees who can access restricted content. 
The contents of the file are based on who is working with personal patient records.
Employees are restricted access based on their IP address. 
There is an allow list for IP addresses permitted to sign into the restricted subnetwork. 
There's also a remove list that identifies which employees you must remove from this allow list.
"""


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

    print("\nIP address allow list parsing complete.")

    print("-----------------\n" + ip_addresses + "\n-----------------")


# Demo reset start
# Resets the `"allow_list.txt"` file to its original contents
# Allows users to demo the file parse script more than once

# Assigns the original contents of the file to the `import_file` variable

if removal_counter > 0:
    import_file = """192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"""

    # Writes `import_file` to the `"allow_list.txt"` file and displays confirmation output
    with open("allow_list.txt", "w") as file:
          file.write(import_file)
          print("allow_list.txt file reset for demo purposes")

# Demo Reset end
