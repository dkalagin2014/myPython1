# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:38:43 2024

@author: IlYA

The task is to calculate the sum of all the checks that we have stored in the file.

"""
import pandas as pd

def calculate_sum(list_num):
    total_sum = 0
    for n in list_num:
        total_sum += n
    return total_sum
    

# Example usage:
filename = 'data.txt'

with open(filename, 'r') as file:
    # Read numbers from the file and convert them to a list of floats
    numbers = [float(x) for x in file.read().split()]

   
    # Calculate the sum of the numbers
    total_sum = calculate_sum(numbers)


 

if total_sum is not None:
    print(f"The sum of numbers from the file {filename} = {total_sum}")


filename = 'data_csv.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(filename, delimiter=';', header=None)

# Extract numbers from the first column and calculate the sum
total_sum2= calculate_sum(df.iloc[:, 0]) 

if total_sum is not None:
    print(f"The sum of numbers from the file {filename} = {total_sum2}")

