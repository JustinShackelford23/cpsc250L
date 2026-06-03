def read_temperatures(filename):
    temperatures = []
    # Formats temperatures as a list
    with open(filename, "r") as file:
        for line in file:
            # reads every line in the file
            if line != "\n":
                # detects if the line is not a null
                number = float(line.strip())
                # Put the line as a float and removes characters then assigns it to number
                temperatures.append(number)
                # Appends number to the list temperature
    return temperatures
    # returns the list of temperatures when done with every line

def calculate_average(values):
    Average = 0.0
    # Assigns average to a float
    for temp in values:
        # Reads every float in values
        Average = Average + temp
        # adds the float number to avg then loops until finished
    Avg = Average / len(values)
    # Does average divided by total numbers in value and assigns to Avg
    return Avg
    # Returns Avg

def find_maximum(values):
    return max(values)
    # Uses the Max function to find the maximum value

def find_minimum(values):
    return min(values)
    # Uses the Min function to find minimum value

def count_above_threshold(values, threshold):
    Hold=0
    # Assigns Hold as a integer
    for temp in values:
        # Reads all values
        if temp > threshold:
            # If the temperature is above the threshold it puts the other line of code
            Hold = Hold + 1
            # Adds one to Hold
    return Hold


def print_report(values):
    avg = calculate_average(values)
    max = find_maximum(values)
    min = find_minimum(values)
    thresh = count_above_threshold(values,80)
    # Uses all the functions and assigned them to names avg, max, min, and thresh
    print("Temperature Report")
    print("------------------")
    print(f"Average temperature: {avg:.1f}")
    print("Maximum temperature:", max)
    print("Minimum temperature:", min)
    print("Temperatures above 80:", thresh)
    # Prints the information with the values from the functions

    pass

def main():
    temperatures = read_temperatures("../data/june_temperatures.txt")
    print_report(temperatures)

main()
