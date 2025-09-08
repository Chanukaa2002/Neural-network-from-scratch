# Build Your Own Neural Network from Scratch

This project demonstrates two ways to build a simple neural network in Python:

- **Fixed Neural Network** (using a simple Neuron class, no learning)
- **Trainable Neural Network** (with manual backpropagation and learning)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Chanukaa2002/Build-own-neural-network.git
cd Build-own-neural-network
```

### 2. Install Requirements

This project only needs `numpy`. Install it with:

```bash
pip install numpy
```

### 3. Run the Examples

#### A. Fixed Neural Network (No Learning)

This uses the `Neuron` and `NeuralNetwork` classes (see comments in `Neuron.py`).

1. Uncomment the relevant code in `Neuron.py` (the `Neuron` and `NeuralNetwork` classes and their usage at the bottom).
2. Run:

```bash
python Fixed_Neural_Network.py
```

#### B. Trainable Neural Network (With Learning)

This uses the `OptimizedNeuralNetwork` class in `Neuron.py`.

1. Make sure the `OptimizedNeuralNetwork` code and its usage at the bottom are uncommented.
2. Run:

```bash
python Neural_Network.py
```

---

## How to Change Inputs

### For the Fixed Neural Network

- Find the lines like:
  ```python
  x = np.array([2,3])
  print(network.feedforward(x))
  ```
- Change the values in the array to your desired input.

### For the Trainable Neural Network

- The training data is defined as:
  ```python
  data = np.array([
  	[-2, -1],
  	[25, 6],
  	[17, 4],
  	[-15, -6],
  ])
  all_true_y = np.array([1, 0, 0, 1])
  ```
- To test new inputs after training, change:
  ```python
  emily = np.array([-7, -3])
  frank = np.array([20, 2])
  print("Emily: %.3f" % network.feedforward(emily))
  print("Frank: %.3f" % network.feedforward(frank))
  ```
- Replace the arrays with your own input values.

---

