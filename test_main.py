import matplotlib.pyplot as plt
import numpy as np

def plot_sine_wave():
    """Generate and plot a sine wave."""
    # Generate the values
    x = np.linspace(-np.pi, np.pi, 201)
    y = np.sin(x)

    # Create the plot
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True)
    plt.show()

# Test the function
if __name__ == "__main__":
    plot_sine_wave()
