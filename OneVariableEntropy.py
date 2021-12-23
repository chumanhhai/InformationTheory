import numpy as np

if __name__ == "__main__":
    source = input("Enter source: ")
    baud = float(input("Enter baud: "))
    charList = [char for char in source]
    characters, occurrence = np.unique(np.array(charList), return_counts=True)
    P = occurrence / len(source)
    H = - np.sum(P*np.log2(P))
    Hmax = - np.log2(1/len(occurrence))
    redundency = Hmax - H
    R = baud * H
    print(len(occurrence))
    print("H(x) =", H)
    print("Redundency =", redundency)
    print("Information rate =", R)

