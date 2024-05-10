import numpy as np

def sig(x):
    return 1 / (1 + np.exp(-x))

def layer(inputs, bias, weights, n):
    outputs = []
    for i in range(n):
        summation = np.sum(weights[i] * inputs) + bias[i]
        y = sig(summation)
        outputs.append(y)
    return outputs

def mlp(inputs, hidden_layer_size, hidden_layer_weights, hidden_layer_bias,
        output_layer_size, output_layer_weights, output_layer_bias, output_layer_target, learning_rate):


    hidden_layer_outputs = layer(inputs, hidden_layer_bias, hidden_layer_weights, hidden_layer_size)

    output_layer_outputs = layer(hidden_layer_outputs, output_layer_bias, output_layer_weights, output_layer_size)


    output_layer_error = output_layer_outputs * (output_layer_target - output_layer_outputs) * (np.ones(output_layer_size) - output_layer_outputs)


    hidden_layer_error = []
    for i in range(hidden_layer_size):
        sum_error = np.sum(output_layer_error * output_layer_weights[:, i])
        hidden_layer_error.append(hidden_layer_outputs[i] * (1 - hidden_layer_outputs[i]) * sum_error)


    for i in range(output_layer_size):
        for j in range(hidden_layer_size):
            output_layer_weights[i][j] += learning_rate * output_layer_error[i] * hidden_layer_outputs[j]
        output_layer_bias[i] += learning_rate * output_layer_error[i]

    for i in range(hidden_layer_size):
        hidden_layer_weights[i] += learning_rate * hidden_layer_error[i] * inputs
        hidden_layer_bias[i] += learning_rate * hidden_layer_error[i]


learning_rate = 0.9
inputs = np.array([1, 0, 1])



hidden_layer_size = np.random.randint(1, 10)
hidden_layer_weights = np.random.uniform(-10, 10, size=(hidden_layer_size, len(inputs)))
hidden_layer_bias = np.random.uniform(-10, 10, size=hidden_layer_size)

output_layer_size = 1
output_layer_target = np.array([1.0])
output_layer_weights = np.random.uniform(-10, 10, size=(output_layer_size, hidden_layer_size))
output_layer_bias = np.random.uniform(-10, 10, size=output_layer_size)


mlp(inputs, hidden_layer_size, hidden_layer_weights, hidden_layer_bias,
    output_layer_size, output_layer_weights, output_layer_bias, output_layer_target, learning_rate)