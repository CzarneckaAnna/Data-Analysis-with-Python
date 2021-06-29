import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    df.plot(x=['Year'], y=['CSIRO Adjusted Sea Level'], kind='scatter')

    # Create first line of best fit
    best_fit = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x = pd.Series([i for i in range(1880, 2051)])
    y = best_fit.slope * x + best_fit.intercept
    plt.plot(x, y, "g")

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    new_best_fit = linregress(x=new_df["Year"], y=new_df['CSIRO Adjusted Sea Level'])
    new_x = pd.Series([i for i in range(2000, 2051)])
    new_y = new_best_fit.slope * new_x + new_best_fit.intercept
    plt.plot(new_x, new_y, 'r')


    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()