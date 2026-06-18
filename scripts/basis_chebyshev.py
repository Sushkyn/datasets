import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load
df = pd.read_csv('data/clean_movies.csv')

print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

numeric_cols = df.select_dtypes(include=[np.number]).columns

print("\n" + "="*60)
print("DESCRIPTIVE STATISTICS")
print("="*60)

#  basic analyzes
for col in numeric_cols:
    data = df[col].dropna()

    mean = data.mean()
    median = data.median()
    variance = data.var()
    std_dev = data.std()

    print(f"\n{col.upper()}")
    print(f"  Mean:        {mean:.2f}")
    print(f"  Median:      {median:.2f}")
    print(f"  Variance:    {variance:.2f}")
    print(f"  Std Dev:     {std_dev:.2f}")
    print(f"  Min:         {data.min():.2f}")
    print(f"  Max:         {data.max():.2f}")

    # chebyshev
    for i in [2, 3, 4]:
        theoretical_min = 1 - (1 / i**2)

        lower_bound = mean - i * std_dev
        upper_bound = mean + i * std_dev

        count_within = ((data >= lower_bound) & (data <= upper_bound)).sum()
        actual_proportion = count_within / len(data)

        print(f"    i={i}:")
        print(f"      Range: [{lower_bound:.2f}, {upper_bound:.2f}]")
        print(f"      Theoretical minimum: {theoretical_min:.2%}")
        print(f"      Actual proportion: {actual_proportion:.2%}")
        print(f"      # Chebyshev holds: {actual_proportion >= theoretical_min}")

print("\n" + "="*60)
