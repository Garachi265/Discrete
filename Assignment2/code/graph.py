import matplotlib.pyplot as plt

# Define the sequence function
def sequence_function(x):
    return (-1) ** (x - 1) * 5 ** (x + 1)

# Values of x
x_values = [0, 1, 2, 3, 4, 5]

# Calculate y values for the sequence
y_values = [sequence_function(x) for x in x_values]

# Plot the sequence
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.title('Sequence: x[n] = (-1)^(n-1) * 5^(n+1)')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

# Annotate points with coordinates
for x, y in zip(x_values, y_values):
    plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(0, 5), ha='center')

plt.show()

