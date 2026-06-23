import pandas as pd
import matplotlib.pyplot as plt


def load_weather_data(filename):
    # TODO: load the data from csv file
    # TODO: return a Pandas dataframe
    dataframe = pd.read_csv(filename)
    return dataframe


def print_summary(df):
    # TODO: print summary statistics
    # TODO: extract the mean temperature and print it
    print(df.describe())
    print()
    print (f'Mean: {(df["high C"].mean() + df["low C"].mean()) /2}')


def add_celsius(df):
    # TODO: add columns for temperatures converted to Celsius
    # TODO: return modified dataframe
    df['high C'] = (df["high"] - 32) / 1.8
    df['low C'] = (df['low'] - 32) / 1.8
    return df

def clean_temperature_range(df, t_low_cut, t_high_cut):
    # TODO: remove days where T_low < t_low_cut or T_high > t_high_cut
    # TODO: return modified dataframe
    df = df[df["high C"] <= t_high_cut]
    df = df[df["low C"] >= t_low_cut]
    return df








def plot_temperatures(df):
    # TODO: plot both high and low temperatures on the same graph
    plt.plot(df["high C"], label="high")
    plt.plot(df["low C"], label="low")
    plt.title('Weather Data')
    plt.xlabel('Day')
    plt.ylabel('Temperature (C)')
    plt.legend()
    plt.show()



def main():

    filename = "../data/weather_june.csv"

    dataframe = load_weather_data(filename)

    dataframe = add_celsius(dataframe)

    T_low_cut = 19.0
    T_high_cut = 31.0
    dataframe = clean_temperature_range(dataframe, T_low_cut, T_high_cut)

    print_summary(dataframe)

    plot_temperatures(dataframe)

main()
#Commit 1: Load and inspect DataFrame
#Commit 2: Add summary statistics
#Commit 3: Add filtering and calculated columns
#Commit 4: Add plot and cleanup