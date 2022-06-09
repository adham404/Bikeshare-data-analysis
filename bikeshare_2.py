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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_valid = False
    month_valid = False
    day_valid = False
    city_list = ["chicago", "new york city", "washington"]
    months_list = ['all','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    days_list = ['all', 'monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while(not city_valid):
        city = input("Please enter the city name: ").lower()
        if(city.lower() in city_list):
            city_valid = True


    # get user input for month (all, january, february, ... , june)
    while(not month_valid):
        month = input("Please enter the month you want (all for all the months): ").lower()
        if(month.lower() in months_list):
            month_valid = True

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while(not day_valid):
        day = input("Please enter the day you want: ").lower()
        if(day.lower() in days_list):
            day_valid = True


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
    days_of_week = ['monday', 'tuesday','wednesday', 'thursday', 'friday','saturday','sunday']

    df = pd.read_csv(CITY_DATA[city])
    # Curating data in the data frame for efficient use in the statistics diplaying functions
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Start Time hour'] = df['Start Time'].dt.hour
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['End Time hour'] = df['End Time'].dt.hour
    df['Travel Time'] = df['End Time hour'] - df['Start Time hour']




    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]



    if day != 'all':
        df = df[df['day_of_week'] == days_of_week.index(day)]




    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    days_of_week = ['monday', 'tuesday','wednesday', 'thursday', 'friday','saturday','sunday']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']




    # display the most common month
    month_mode = df['month'].mode()[0] 
    print('Most common month: ' + months[month_mode - 1])


    # display the most common day of week
    mode = df['day_of_week'].mode()[0]
    print('Most common day of the week: ' + days_of_week[mode])

    # display the most common start hour
    popular_hour = df['Start Time hour'].mode()[0]
    print('Most Popular Start Hour: (in 24 hour clock system) ', popular_hour )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most common start station: ' + df['Start Station'].mode()[0])


    # display most commonly used end station
    print('Most common end station: ' + df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['Start End Combination'] = df['Start Station'] + df['End Station']
    print('Most common Start and End Station combination: ' + df['Start End Combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time: " + str(df['Travel Time'].sum()) + ' hours')


    # display mean travel time
    print("Mean Trave Time: " + str(round(df['Travel Time'].mean(),4)) + ' hours')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def remove_last_line_from_string(s):
    return s[:s.rfind('\n')]


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = str(df['User Type'].value_counts())
    print("Counts of user types\n" + remove_last_line_from_string(user_types))


    #creating spaces between output statistics
    print("\n\n")



    # Display counts of gender
    try:
        user_gender = str(df['Gender'].value_counts())
        print("Counts of user gender\n" + remove_last_line_from_string(user_gender))
    except:
        print("******************************************* Important Note ********************************************")
        print("\n")
        print("Unfortunately this data ---------------Gender----------------- is not provided for this city....")
        print("\n")
        print("*******************************************************************************************************")

    #creating spaces between outhput statistics
    print("\n\n")

    
    # Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print("Earlist birth year: " + str(int(earliest)) + '\n' + "Most recent birth year: " + str(int(most_recent)) + '\n' + "Most common birth year: " + str(int(most_common)) )
    except:
        print("******************************************* Important Note ********************************************")
        print("\n")
        print("Unfortunately this data ---------------Birth Year----------------- is not provided for this city....")
        print("\n")
        print("*******************************************************************************************************")

    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data == "yes"):
        print(df.iloc[start_loc : start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: (Please enter yes or no) ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
