#!/usr/bin/env python3.7

#AWS Service Inventory

# Create a list of services using Python. IE: S3, Lambda, EC2, etc

# 1. The list should be empty initially.
# 2. Populate the list using append or insert.
# 3. Print the list and the length of the list.
# 4. Remove two specific services from the list by name or by index.
# 5. Print the new list and the new length of the list.

# Create an empty list. 

aws_services = [ ]

# Populate the list using append or insert. 
aws_services.append('EC2')
aws_services.append('S3')
aws_services.append('Lambda')
#Populate the list using insert. 
aws_services.insert(1, "VPC")
aws_services.insert(3, "DynamoDB")
aws_services.insert(6, "Kinesis")

#Print the list and the length of the list.
print(aws_services)
print(len(aws_services))

#Remove two specific services from the list by name or by index.
del aws_services[1]
aws_services.remove("Lambda")

#Print the new list and the new length of the list.
print(aws_services)
print(len(aws_services))