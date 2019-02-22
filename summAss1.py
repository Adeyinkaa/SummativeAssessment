# To generate random numbers between 0 and 1
import random

import datetime

# Create an list to hold the 16 floats
sensor_list = [0] * 16

# Create a variable to hold the name of each Sensor
a = "Sensor"

# Create empty dictionary to hold generated sensor data
sensor_data = {}

# Generate a list within a dictionary to associate several values to the key
n = 1
while n < 33:
    sensor_data.update({a+str(n):sensor_list})
    n += 1
print(sensor_data)

# Create a for loop to iterate over the values in the dictionary
count = 15
for output in sensor_data.values():
    while count > -1:
        # Create an indexed variable to hold each random number generated
        output[count] = random.random()
        count -= 1
print(sensor_data)

# Create a variable to hold the text file
filename = "output_data.txt"

# Use the append mode to open the file so data is not overwritten
# Python closes the file when using "with open"

with open(filename, 'a') as out_file:
    for i, v in sensor_data.items():
      print(sensor_data)
# Write to the file
# Data stream will be written to the filename, "output_data.txt"
    out_file.write(str(sensor_data))

# Loop over indexed values in the list
for value in sensor_data.values():
    for i in range(0, len(value)):
        # Define condition to include corrupt data
        if 0.15 > value[i] < 0.3:
        # Set the corrupt value
            value[i] = 1000000000
print(sensor_data)

# Write output to file

now = datetime.datetime.now()
filename = "error_log.txt"
with open(filename, "a") as outfile2_output:
    outfile2_output.write(str(sensor_data))

# Define function to test for corrupt data

def test_error(sensor_data):

# use enumerate function to identify sensor with corrupt data

    for index, (k, v) in enumerate(sensor_data.items()):
        index = index + 1
        for i in range(0, len(v)):
            # Check for corrupt data
            if v[i] == 1000000000:
            # Print error that identifies sensor with corrupt dara
                print("Error on Sensor {}".format(index))

# Call the function to test for the error
test_error(sensor_data)






















