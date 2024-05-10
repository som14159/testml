def mp(w1, w2, x1, x2):
    activation = x1 * w1 + x2 * w2
    if activation >= 2:
        return 1
    else:
        return 0

def main(): 
    w1 = float(input("Enter the weight w1: "))
    w2 = float(input("Enter the weight w2: "))

    print("\nAND Gate:")
    print("x1 | x2 | y | f(x) | y_out")
    print("-----------------------------")
    for x1 in range(2):
        for x2 in range(2):
            fx = int(w1 * x1 + w2 * x2)
            y = x1 & x2
            y_out = mp(w1, w2, x1, x2)
            print(f"{x1} | {x2} | {y} | {fx} | {y_out}")

    print("\nOR Gate:")
    print("x1 | x2 | y | f(x) | y_out")
    print("-----------------------------")
    for x1 in range(2):
        for x2 in range(2):
            fx = int(w1 * x1 + w2 * x2)
            y = x1 | x2
            y_out = mp(w1, w2, x1, x2)
            print(f"{x1} | {x2} | {y} | {fx} | {y_out}")

main()
