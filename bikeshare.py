import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('would you like to explore data for chicago , new york city or washington?').lower()
        if city in CITY_DATA:
             print(city)
             break
        else:
            print('sorry your input was invalid. please input either chicago , new york or washington.')
    # TO DO: get user input for month (all, january, february, ... , june)
    months = {"january":1 , "february":2 , "march":3 , "april":4 , "may":5 , "june":6 , "all":"all"}
    month = input("choose the month you want to do analysis on:january , february , march ,april ,may , june or all ?").lower()
    month = months[month]
    print(month)
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday' ,'sunday' ,'monday','tuesday','wednesday','thursday','friday','all']
    while True:
        day= input('enter the day of the week . sunday ,monday,tuesday , wednesday, thursday,friday?').lower()
        if day in days:
            print(day)
            break
        else:
            print('sorry your input was invalid. Choose the right day in this format: saturday, sunday etc')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"]= pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour
    
    if month != "all":
        df = df[df["month"] == month]
        
    if day != "all":
        df = df[df["day"] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df["month"].value_counts().idxmax()
    print("the month is:", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df["day"].value_counts().idxmax()
    print("the common day is:", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df["hour"].value_counts().idxmax()
    print("the start hour is:", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df["Start Station"].value_counts().idxmax()
    print("the most commonly used start station is:", commonly_start_station)

    # TO DO: display most commonly used end station
    commonly_end_station = df["End Station"].value_counts().idxmax()
    print("the most commonly used end station is:", commonly_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = (df["Start Station"] + " - " + df["End Station"]).value_counts().idxmax()
    print("the most commonly most frequent combination of start station and end station trip is:", most_frequent_combination )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("total travel time is:", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("mean travel time is:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df["User Type"].value_counts()
    print(user_type)

    # TO DO: Display counts of gender
    if "Gender" in df:
        gender = df["Gender"].value_counts()
        print(gender)
    else:
        print("no gender input!")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
      earliest_year = df["Birth Year"].min()
      print(" the earliest year:", earliest_year)
      recent_year = df["Birth Year"].max()
      print(" the most recent year:", recent_year)
      brith_year = df["Birth Year"].mode()[0]
      print(" the birth year:", brith_year)
    else:
        print('no birth year input')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        y = 5
        while True:
              print(df.iloc[y-5: y])
              y += 5
              result = input('if you want to see more data inter yes else inter no?')
              if result.lower() == 'no':
                   break
                    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
