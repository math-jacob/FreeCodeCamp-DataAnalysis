import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('D:/Cursos/Data/FreeCodeCamp-DataAnalysis/Projects/Project4/data/fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, axes = plt.subplots(figsize=(20, 5))

    axes.plot(df.index, df['value'], color='red')

    axes.set_xlabel('Date')
    axes.set_ylabel('Page Views')
    axes.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('D:/Cursos/Data/FreeCodeCamp-DataAnalysis/Projects/Project4/images/line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(by=['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    fig = df_bar.plot.bar(legend=True, figsize=(13, 6), ylabel='Average Page Views', xlabel='Years').figure

    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=13)

    # Save image and return fig (don't change this part)
    fig.savefig('D:/Cursos/Data/FreeCodeCamp-DataAnalysis/Projects/Project4/images/bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box = df_box.sort_values(by='month', ascending=True)
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 5))

    axes[0] = sns.boxplot(x=df_box['year'], y=df_box['value'], ax=axes[0], linewidth=0.5)
    axes[1] = sns.boxplot(x=df_box['month'], y=df_box['value'], ax=axes[1], linewidth=0.5)

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('D:/Cursos/Data/FreeCodeCamp-DataAnalysis/Projects/Project4/images/box_plot.png')
    return fig
