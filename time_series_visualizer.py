import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
rem_top_outliers = df['value'] <= df['value'].quantile(0.975)
rem_bot_outliers = df['value'] >= df['value'].quantile(0.025)

df = df[rem_top_outliers & rem_bot_outliers]


def draw_line_plot():
    # Draw line plot
    df['date'] = pd.to_datetime(df['date'])
    fig, ax = plt.subplots(figsize=(12,4))
    ax.plot(df['date'], df['value'], color='r', linewidth=1)
    ax.set_title('Daily FreeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    data = df.copy()
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    df_bar = data.groupby(['year','month'])['value'].mean().unstack()

    # Get month names
    month_names = [calendar.month_name[i] for i in range(1, 13)] 

    # Draw bar plot
    fig,ax = plt.subplots(figsize=(10,6))
    df_bar.plot(kind='bar',ax=ax)
    ax.set_title('Average Daily Page Views')
    ax.legend(labels=month_names, title='Months', loc='upper left')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
