if __name__ == "__main__":
    numberOfSymbol = int(input("Enter number of symbol: "))
    H = float(input("Enter H(x) = "))
    Hmax = float(input("Enter H(x) max = "))
    no = float(input("Enter n0 = "))
    I = numberOfSymbol * H
    C = no * Hmax
    t = I / C
    print("t =", t)