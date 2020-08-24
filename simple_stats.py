import math

def getNums():
    numbers = input("> ")
    numbers = numbers.replace(" ", "")
    numbers = numbers.split(",")
    return numbers


def format(numbers):
    for i in range(len(numbers)):
        try:
            numbers[i] = float(numbers[i])
        except:
            numbers.remove(numbers[i])

    return numbers

def getMean(numbers):
    sum = 0
    for ele in numbers:
        sum += ele
    mean = sum / len(numbers)
    return mean

def getMedian(numbers):

    numbers.sort()
    nlen = len(numbers)

    if nlen % 2 == 0:
        median = (numbers[int((nlen - nlen/2))] + numbers[int(nlen/2 - 1)]) / 2
        return median
    else:
        median = numbers[int((nlen-1) / 2)]
        return median

def getMode(numbers):
    num_count = {}
    for ele in numbers:
        if ele in num_count:
            num_count[ele] += 1

        else:
            num_count[ele] = 1

    mode = max(num_count)
    return mode

def getRange(numbers):
    numbers.sort()
    range = math.fabs(numbers[0] - numbers[(len(numbers))-1])
    return range
def getDeviation(numbers):
    sum = 0
    for ele in numbers:
        sum += ele

    mean = sum / len(numbers)
    variance_sum = 0
    for n in numbers:
        difference = n - mean
        variance_sum += ((math.fabs(difference)) ** 2)


    variance_mean = variance_sum/len(numbers)


    deviation = math.sqrt(variance_mean)
    return deviation

def getError(deviation, numbers):

    standard_error = deviation / (math.sqrt(len(numbers)))
    return standard_error

def solve():
    numbers = getNums()
    numbers = format(numbers)
    mean = getMean(numbers)
    median = getMedian(numbers)
    mode = getMode(numbers)
    range = getRange(numbers)
    deviation = getDeviation(numbers)
    error = getError(deviation, numbers)
    print("Mean: {}".format(mean))
    print("Median: {}".format(median))
    print("Mode: {}".format(mode))
    print("Range: {}".format(range))
    print("Standard Deviation: {}".format(deviation))
    print("Standard Error: +-{}".format(error))

solve()