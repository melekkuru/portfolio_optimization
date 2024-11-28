
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_results(std_devs, exp_returns, title, filename):
    '''
    Plot the Efficient Frontier and save the plot to a file.
    '''
    # Ensure the plots directory exists
    os.makedirs("plots", exist_ok=True)

    min_risk_index = np.argmin(std_devs)
    min_volatility = std_devs[min_risk_index]
    min_return = exp_returns[min_risk_index]

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(std_devs, exp_returns, color='black', label='Portfolio Optimization Results')
    ax.scatter(min_volatility, min_return, color='yellow', label='Minimum Risk Portfolio')
    ax.annotate('Minimum Risk Portfolio', (min_volatility, min_return), 
                xytext=(-50, 30), textcoords='offset points',
                arrowprops=dict(facecolor='black', arrowstyle='->'))
    ax.set_xlabel('Standard Deviation (𝜎)')
    ax.set_ylabel('Expected Return (𝜇)')
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

    # Save the plot
    plot_path = os.path.join("plots", filename)
    plt.savefig(plot_path)
    print(f"Plot saved to {plot_path}")
    plt.show()
