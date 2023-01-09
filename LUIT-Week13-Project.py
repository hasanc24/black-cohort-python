#LUIT Week 13 Project 

                                        #EC2 Random Name Generator

#Several departments share an AWS environment. 
#You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. 
#Use Python to create your unique EC2 names that the users can then attach to the instances. 

#The Python Script should:

# 1: All the user to input how many EC2 instances they want names for and output the same amount of unique names.
# 2: Allow the user to input the name of their department that is used in the unique name.
# 3: Generate random characters and numbers that will be included in the unique name.

import time 
import random
import string

# Random name Funcation Generator 
def string_generator(size=6, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))

department = input("Enter the department name Accounting, FinOps, or Marketing.\n").upper()

for _ in department:
    
    if department == "Marketing" or department.lower() == "marketing":
        print("Please wait verifying the Department")
        time.sleep(10)
        break
    
    elif department == "FinOps" or department.lower() == "finops":
        print("Verification in process, please wait...")
        time.sleep(10)
        break
    
    elif department == "Accounting" or department.lower() == "accounting":
        print("Processing, one please wait...")
        time.sleep(10)
        break
    
    else:
        print("Error : Department could not be verified. Enter the correct Department for access.")
        raise TimeOut
        time.sleep(10)  

number = int(input("Input the number of EC2 instances that require names: "))
    
if number < 0:
    print("Please enter at least one number: ")
elif number > 0:
    print("Request accepted")
    
#Results should be printed
print("\n...Processing Request Please Wait...\n")
time.sleep(10)
print("Here are your results!!")

for _ in range(1, number + 1):
    EC2_name = department
    unique_name = EC2_name + "-" + string_generator()
    print("Your New EC2 Instance Name : ", unique_name)
    
print("Success! Thank you for using the name generator!!")