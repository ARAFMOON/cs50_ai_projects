import csv

# Open the CSV file
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        print(row)


import pandas as pd

# Read the CSV file
data = pd.read_csv('data.csv')

# Display the data
print(data)
