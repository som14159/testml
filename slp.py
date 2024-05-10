import numpy as np

def single_layer_perceptron(inputs, outputs, learning_rate, weights):
    for i in range(len(inputs)):
        summation = np.sum(weights * inputs[i])
        y_output = 1 if summation > 0 else 0
        error = outputs[i] - y_output
        weights += learning_rate * error * inputs[i]


def test(inputs, outputs, weights):
    for i in range(len(inputs)):
        for j in inputs[i]:
            print(j, end="\t")
        print(outputs[i], end="\t")
        summation = np.sum(weights * inputs[i])
        print("{:.1f}".format(summation), end="\t")
        y_output = 1 if summation > 0 else 0
        print(y_output, end="\t")
        print()

    print("\nActivation Function: \nY = 1 if F(x) > 0 \nY = 0 if F(x) <= 0 ")

or_gate_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
bias_inputs = [np.append(x,1) for x in or_gate_inputs]
or_gate_outputs = np.array([0, 1, 1, 1])
learning_rate = float(input("Enter learning rate: "))
weights = np.array([0.0, 0.0, 0.0])
flag = True
i = 1

while flag:
    i += 1
    prev_weight = weights.copy()
    single_layer_perceptron(bias_inputs, or_gate_outputs, learning_rate, weights)
    if np.array_equal(prev_weight, weights, equal_nan=True):
        flag = False

test(bias_inputs, or_gate_outputs, weights)
