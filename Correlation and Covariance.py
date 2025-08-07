import pandas as pd

data = {
    'Physics': [85, 72, 90, 66, 95],
    'Maths': [92, 88, 84, 75, 91],
    'Chemistry': [78, 80, 65, 70, 60]
}

df = pd.DataFrame(data)

# Correlation matrix
print("Correlation Matrix:\n", df.corr())

# Covariance matrix
print("\nCovariance Matrix:\n", df.cov())

