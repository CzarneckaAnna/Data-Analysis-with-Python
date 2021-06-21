import datetime

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime as dt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", sep=",")

# Clean data (2,5%)
clean_nbr = int(round(df['value'].count() * 0.025, 0))

df = df.sort_values('value')[clean_nbr:-clean_nbr]
df = df.sort_values('date')


def draw_line_plot():
    # Draw line plot
    fig = plt.figure()
    plt.plot(df['date'], df['value'])

    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df[['year', 'month', 'Day']] = df.date.str.split("-", expand=True)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = [d.strftime('%B') for d in df.date]
    df_bar = df[['year', 'month', 'value']]
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().reset_index(name='Average Page Views')


    # Draw bar plot
    df_bar = df_bar.pivot(index='year', columns='month', values='Average Page Views')
    print(df_bar)
    fig = df_bar.plot(kind="bar").figure
    plt.ylabel("Average Page Views")
    plt.xlabel("Year")
    # plt.legend(fontsize=10, title="Months",
    #            labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
    #                    'Nov','Dec'])

    plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df['date'] = pd.to_datetime(df['date'])
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    ax1 = sns.boxplot(ax=axes[0], data=df_box, x='year', y='value')
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2 = sns.boxplot(ax=axes[1], data=df_box, x='month', y='value')
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    # fig = sns.boxplot(x=df["year"], y=df["value"]).figure


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
