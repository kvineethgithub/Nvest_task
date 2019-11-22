import random
import csv
import math

# open the csv file and read the data and store into dataSet
try:
    with open('iris.csv') as file:
        reader = csv.reader(file)
        data_set = list(reader)
        dataSet = data_set[1:]
        # shuffle the data for random data from list
        random.shuffle(dataSet)
        # div is a variable for particular range to divide dataSet
        div = int(0.66 * len(dataSet))
        train = dataSet[1:div]
        test = dataSet[div:]
except Exception as e:
    print(e)


# square root of the sum of the squared differences between the two arrays of numbers
def euclidean_distance(instance1, instance2, length):
    try:
        distance = 0
        for i in range(length):
            s = float(instance1[i]) - float(instance2[i])
            distance += s ** 2
        return math.sqrt(distance)
    except Exception as error:
        print(error)


# distances = []
def get_neighbors(training_set, test_instance, k):
    try:
        distances = []
        length = len(test_instance) - 1
        for i in range(len(training_set)):
            dist = euclidean_distance(test_instance, training_set[i], length)
            distances.append((training_set[i], dist))
        distances.sort()
        neighbours = []
        for i in range(k):
            neighbours.append(distances[i][0])
        return neighbours
    except Exception as error:
        print(error)


classVotes = {}


def get_response(neighbours):
    # classVotes = {}
    try:
        for i in range(len(neighbours)):
            response = neighbours[i][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sorted_votes = sorted(classVotes.items(), reverse=True)
        return sorted_votes[0][0]
    except Exception as error:
        print(error)


def get_accuracy(test_set, prediction_set):
    try:
        correct = 0
        for i in range(len(test_set)):
            if test_set[i][-1] == prediction_set[i]:
                correct += 1
        return (correct / float(len(test_set))) * 100.0
    except Exception as error:
        print(error)


predictions = []
p = 3
for x in range(len(test)):
    # print(len(test[x]))
    neighbors = get_neighbors(train, test[x], p)
    # print("N",neighbors)
    result = get_response(neighbors)
    # print("R",result)
    predictions.append(result)
    # print(predictions)
    print('predicted=' + repr(result) + '  actual=' + repr(test[x][-1]))

accuracy = get_accuracy(test, predictions)
print()
print('Accuracy: ' + repr(accuracy) + '%')
