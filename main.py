import csv


def printArray(parArray):
    for i in parArray:
        print(i)


def printSCVFile(parNameFile):
    with open(parNameFile) as scvFile:
        reader = csv.reader(scvFile)
        for row in reader:
            print(row[1])


def getSizeDataSet(parNameFile):
    with open(parNameFile) as scvFile:
        reader = csv.reader(scvFile)
        return sum(1 for row in reader)


# Car Name,
# Engine Type,
# Engine Alignment,
# Fuel Type,
# Number of Valves,
# Engine Size,
# Compression Ratio,
# Maximum Power,
# Maximum Torque,
# Drivetrain,
# Transmission Gearbox,
# Fuel Consumption,
# Range,
# Fuel Tank Capacity,
# CO2 Emissions,
# Top Speed,
# Acceleration 0 to 100 km/h,
# Number Of Doors,
# Wheelbase,
# Length,
# Width,
# Height,
# Curb Weight,
# Weight-Power Output Ratio,
# Boot capacity

# dataSet = [1, 2, 3, 4, 5, 6]
nameFile = 'data/cars_dataset.csv'

# printArray(dataSet)
# printSCVFile(nameFile)
print(getSizeDataSet(nameFile))
