import numpy as np

def readMatrix(name):
    matrix = input("Enter " + name +": ").split(" ")
    matrix = [float(value) for value in matrix]
    matrix = np.array(matrix)
    return matrix

if __name__ == "__main__":
    pi = readMatrix("pi")
    size = int(np.sqrt(len(pi)))
    pi = pi.reshape(size, size)

    Wt = readMatrix("W0")
    Wt = Wt.reshape(len(Wt), 1)

    for i in range(1, 6):
        Wt = pi.dot(Wt)
        print("W" + str(i) + " = ", Wt)