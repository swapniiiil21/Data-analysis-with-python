import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data", color="blue")

    # First line of best fit (1880–2050)
    res1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = res1.intercept + res1.slope * x_pred1
    plt.plot(x_pred1, y_pred1, 'r', label="Best fit: All data")

    # Second line of best fit (2000–2050)
    df_recent = df[df["Year"] >= 2000]
    res2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = res2.intercept + res2.slope * x_pred2
    plt.plot(x_pred2, y_pred2, 'green', label="Best fit: 2000 onwards")

    # Labels & title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()

    # Save & return
    plt.savefig('sea_level_plot.png')
    return plt.gca()
