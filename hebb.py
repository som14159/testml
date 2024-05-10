import numpy as np

def bipolarizeInput(inputs):
    return np.where(inputs == 0, -1, inputs)

def or_gate_hebbian_learning(inputs, outputs):
    num_inputs = len(inputs[0])
    weights = np.zeros(num_inputs)
    
    for i in range(len(inputs)):
        weights += inputs[i] * outputs[i]

    print("Weights : ")
    for i in range(len(weights)):
        if i == len(weights) - 1:
            print(f"wb = {weights[i]}")
        else:
            print(f"w{i+1} = {weights[i]}")

    flag = False
    threshold = 0

    print("\nX1\tX2\tXb\tF(x)\tY")
    for i in range(len(inputs)):
        for j in inputs[i]:
            if j > 0:
                print("+", end="")
            print(j, end="\t")

        summation = np.sum(weights * inputs[i])
        if summation > 0:
            print("+", end="")
        print(summation, end="\t")

        if outputs[i] > 0:
            print("+", end="")
        print(outputs[i])

        if outputs[i] == 1 and not flag:
            threshold = summation
            flag = True

    print("\nActivation Function : \nY = +1 if F(x) >= ", threshold, "\nY = -1 if F(x) < ", threshold)

or_gate_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
bipolarized_inputs = bipolarizeInput(np.c_[or_gate_inputs, np.ones(len(or_gate_inputs))])
or_gate_outputs = np.array([0, 1, 1, 1])
bipolarized_outputs = np.where(or_gate_outputs == 0, -1, or_gate_outputs)

or_gate_hebbian_learning(bipolarized_inputs, bipolarized_outputs)
