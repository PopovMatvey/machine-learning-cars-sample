import csv


# Получить выборку
def getSample(parPathToFile):
    returnedAray = []
    with open(parPathToFile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            returnedAray.append(row)
    return returnedAray


# Получить  размер
def getSizeSample(parPathToFile):
    with open(parPathToFile) as csvfile:
        reader = csv.DictReader(csvfile)
        return sum(1 for row in reader)


# Вывести массив
def printAray(parArray):
    for row in parArray:
        print(" " + row + " \n")


pathToFile = 'data/cars_dataset.csv'
carSample = getSizeSample(pathToFile)

# print(getSizeSample(pathToFile))
print(getSample(pathToFile))
printAray(carSample)