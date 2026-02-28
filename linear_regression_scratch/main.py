import numpy as np
import pandas as pd
import math


class LINEAR_REGRESSION_SCRATCH:
    def __init__(self, learning_rate, convergence_tool= 1e-6):
        self.learning_rate = learning_rate
        self_convergence_tool = convergence_tool
        self.W = None
        self.b = None


    def fit(self):
        pass


    def standardize_data(self, X_train, X_test):
        mean = np.mean(X_train, axis=0)
        std = np. std(X_train, axis=0)

        X_train = (X_train - mean) / std
        X_test = (X_test - mean) / std

        return X_train, X_test