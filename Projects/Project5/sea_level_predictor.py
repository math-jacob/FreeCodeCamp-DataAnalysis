import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    
    # Read data from file
    df = pd.read_csv('D:/Cursos/Data/FreeCodeCamp-DataAnalysis/Projects/Project5/data/epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, axes = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x=x, y=y)
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.slope*x_pred + res.intercept
    plt.plot(x_pred, y_pred, color='red')

    # Create second line of best fit
    new_df = df.loc[df['Year'] >= 2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    res2 = linregress(x=new_x, y=new_y)
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = res2.slope*x_pred2 + res2.intercept
    plt.plot(x_pred2, y_pred2, color='green')

    # Add labels and title
    axes.set_title('Rise in Sea Level')
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('D:/Cursos/Data/FreeCodeCamp-DataAnalysis/Projects/Project5/images/sea_level_plot.png')
    return plt.gca()