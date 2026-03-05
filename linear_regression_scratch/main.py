import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd
# import math


class LinearRegressionScratch:
    def __init__(self, learning_rate= 0.01, n_iters= 1000):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.W = None
        self.b = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.W = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iters):
            y_pred = np.dot(X, self.W) + self.b
            error = y_pred - y

            dw = (1/n_samples) * np.dot(X.T, error)
            db = (1/n_samples) * np.sum(error)

            self.W = self.W - self.learning_rate * dw
            self.b = self.b - self.learning_rate * db


    def predict(self, X):
        y_pred = np.dot(X, self.W) + self.b
        return y_pred


    def mse(self, y_test, predictions):
        return np.mean((y_test-predictions)**2)


