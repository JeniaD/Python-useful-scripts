import matplotlib.pyplot as plt #Additionally. GuessLinearFunc can work without it.
import random

#Additionally. GuessLinearFunc can work without it.
def ShowGraph(x1, y1, x2, y2):
    plt.plot(x1, y1, label = "Dataset") 
 
    plt.plot(x2, y2, label = "Guessed result") 
  
    plt.xlabel("x axis") 
    plt.ylabel("y axis") 
    plt.title("Prediction") 
  
    plt.legend() 
  
    plt.show()

def ErrorAverage(k, b, x, y):
    error = 0
    for index in range(len(x)):
        error = error + ((k*x[index] + b) - y[index]) / 2
    
    return error

def Module(x):
    if x < 0:
        return x * -1
    else:
        return x
#Function that returning array [k, b, errorAverage] of function f(x) = kx + b.
#Dont calculating good if k or x is non-integer. minRange is not implemented yet.
def GuessLinearFunc(Xtrain, Ytrain, maxRange, minRange):
    k = minRange
    b = minRange
    results = [[[0 for _ in range(maxRange)] for _ in range(maxRange)] for _ in range(maxRange)]
    merr = 1000000

    for testK in range(maxRange):
        for testB in range(maxRange):
            for res in range(maxRange):
                results[testK][testB][res] = ErrorAverage(testK, testB, Xtrain, Ytrain)
                if Module(results[testK][testB][res]) < Module(merr):
                    merr = results[testK][testB][res]
                    k = testK
                    b = testB

    return [k, b, merr]
   
#Usage:
'''
xTrainExample = [1, 2, 3, 4, 5]
yTrainExample = [3, 5, 7, 9, 11]
#In function f(x) = kx + b:
maxRange = 100 #Max k and b.
minRange = 0 #Minimum possible k or b. Not implemented yet.
result = GuessLinearFunc(xTrainExample, yTrainExample, maxRange, minRange)
#k is result[0]
#b is result[1]
#Error average is result[2]

#Additionally:
x2 = [None] * exampleLength
y2 = [None] * exampleLength
for index in range(len(x2)):
  x2[index] = x[index]
  y2[index] = x[index]*prediction[0] + prediction[1]
ShowGraph(x, y, x2, y2)
'''
