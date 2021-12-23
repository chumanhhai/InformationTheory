import numpy as np

if __name__ == "__main__":
    size = int(input("Enter size: "))
    Px = np.empty(size, float)
    Py = np.empty(size, float)
    Pxy = np.empty((size, size), float)
    for i in range(0, size-1):
        Px[i] = float(input("Enter P(x"+str(i)+"): "))
    Px[-1] = 1 - np.sum(Px[:-1])
    matrix = input("Enter matrix: ").split(" ")
    matrix = [float(value) for value in matrix]
    matrix = np.array(matrix).reshape(size, size)

    for i in range(0, size):
        for j in range(0, size):
            Pxy[i][j] = matrix[i][j] * Px[i]
    Hy_x = -np.sum(Pxy * np.log2(matrix))
    Hx = -np.sum(Px * np.log2(Px))
    Hxy = Hx + Hy_x
    Py = np.sum(Pxy, 0)
    Hy = -np.sum(Py * np.log2(Py))
    Hx_y = Hxy - Hy
    Ixy = Hy - Hy_x
    print("H(x) =", Hx)
    print("H(y) =", Hy)
    print("H(x|y) =", Hx_y)
    print("H(y|x) =", Hy_x)
    print("H(x,y) =", Hxy)
    print("I(x;y) =", Ixy)

