
# **Portfolio Optimization**

This project demonstrates various portfolio optimization strategies to balance risk (variance) and return using Python and Gurobi. The project explores four distinct tasks that represent common scenarios in investment portfolio management.

---

## **Features**
1. **Task 1:** Fully invested portfolios (sum of allocations = 1).
2. **Task 2:** Partial investment portfolios (sum of allocations ≤ 1).
3. **Task 3:** Portfolios with a target return constraint (return ≥ target).
4. **Task 4:** Portfolios allowing short selling (negative allocations allowed).

Each task generates an efficient frontier, showcasing the trade-off between risk and return.

---

## **Getting Started**

Follow these instructions to set up and run the project on your local machine.

### **Prerequisites**
- Python 3.8 or higher
- Gurobi installed and licensed
- Virtual environment (optional but recommended)

---

### **Setup Instructions**

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-username/portfolio-optimization.git](https://github.com/melekkuru/portfolio_optimization)
   cd portfolio-optimization
   ```

2. **Create and Activate a Virtual Environment:**
    ```
    python -m venv venv
   source venv/bin/activate    # For macOS/Linux
   venv\Scripts\activate       # For Windows (Command Prompt)
   .\venv\Scripts\Activate     # For Windows (PowerShell)
    ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Project:**
   Execute the `main.py` script to run all tasks:
   ```bash
   python main.py
   ```

---

## **Project Structure**

```
portfolio_optimization/
│
├── src/                # Source code for individual tasks and utilities
│   ├── task1.py        # Task 1: Fully invested portfolios
│   ├── task2.py        # Task 2: Partial investment portfolios
│   ├── task3.py        # Task 3: Target return portfolios
│   ├── task4.py        # Task 4: Portfolios with short selling
│   ├── utils.py        # Shared utilities (e.g., plotting)
│
├── notebook/           # Jupyter Notebook for interactive analysis
│   └── portfolio_optimization.ipynb
│
├── plots/              # Folder to store generated plot images
│   ├── task1_plot.png
│   ├── task2_plot.png
│   ├── task3_plot.png
│   └── task4_plot.png
│
├── README.md           # Documentation for the project
├── requirements.txt    # Required Python libraries
├── main.py             # Main script to execute all tasks
```

---

## **Results**

Each task generates a plot of the efficient frontier, visualizing the trade-off between risk and return for various portfolio configurations:
- **Task 1:** Fully invested portfolios.
- **Task 2:** Partial investment portfolios.
- **Task 3:** Portfolios meeting or exceeding a target return.
- **Task 4:** Portfolios allowing short selling.

### **Example Plot**
![task1_plot](https://github.com/user-attachments/assets/f8544705-b1f8-42ad-9ee4-b3ccfc2963b5)


---

