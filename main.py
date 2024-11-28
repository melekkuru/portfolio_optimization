
from src.task1 import run_task1
from src.task2 import run_task2
from src.task3 import run_task3
from src.task4 import run_task4
from src.utils import plot_results

if __name__ == "__main__":
    # Run Task 1
    std_devs1, exp_returns1 = run_task1()
    plot_results(std_devs1, exp_returns1, "Task 1: Portfolio Optimization Results", "task1_plot.png")

    # Run Task 2
    std_devs2, exp_returns2 = run_task2()
    plot_results(std_devs2, exp_returns2, "Task 2: Portfolio Optimization Results (Partial Investment)", "task2_plot.png")

    # Run Task 3
    std_devs3, exp_returns3 = run_task3()
    plot_results(std_devs3, exp_returns3, "Task 3: Portfolio Optimization Results (Target Return >= Constraint)", "task3_plot.png")

    # Run Task 4
    std_devs4, exp_returns4 = run_task4()
    plot_results(std_devs4, exp_returns4, "Task 4: Portfolio Optimization Results (Short Selling Allowed)", "task4_plot.png")
