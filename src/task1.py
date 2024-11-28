
import gurobipy as gp
from gurobipy import GRB
import numpy as np
from math import sqrt

def run_task1():
    '''
    Task 1: Basic Portfolio Optimization
    Minimize portfolio risk under the constraint that allocations sum to 1.
    '''
    # Problem Parameters
    n = 8  # Number of assets
    np.random.seed(2315873)
    Corr = np.array([[(-1) ** abs(i - j) / (abs(i - j) + 1) for j in range(n)] for i in range(n)])
    ssigma = np.cumsum(np.random.uniform(0.5, 1.5, n)).reshape(-1, 1)
    mmu = np.arange(3, 3 + n).reshape(-1, 1)

    ddiag = np.diag(ssigma.flatten())
    C2 = ddiag @ Corr @ ddiag
    C = 0.5 * (C2 + C2.T)  # Ensure symmetry

    # Initialize Gurobi Model
    m = gp.Model('portfolio')
    x = m.addMVar(n, lb=0.0, ub=1.0, vtype=GRB.CONTINUOUS, name='x')

    # Objective: Minimize portfolio variance
    portfolio_risk = x @ C @ x
    m.setObjective(portfolio_risk, GRB.MINIMIZE)

    # Constraints
    m.addConstr(x.sum() == 1, 'budget')

    # Solve for different target returns
    optimal_allocations = []
    target_returns = np.arange(3.00, 9.25, 0.25)  # Target returns (mu)

    for target_return in target_returns:
        target_return_constraint = m.addConstr(mmu.T @ x == target_return, 'target_return')
        m.optimize()

        if m.status == GRB.OPTIMAL:
            optimal_allocations.append(x.X)

        m.remove(target_return_constraint)

    # Analyze Results
    std_devs = [sqrt(np.dot(opt, np.dot(C, opt))) for opt in optimal_allocations]
    exp_returns = [np.dot(mmu.flatten(), opt) for opt in optimal_allocations]

    return std_devs, exp_returns
