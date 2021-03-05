import time
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    city = get_city()
    filter_type = input('Would you like to filter the data by month (enter m), day (enter d), both (enter b) or not at all (enter anything else or nothing)?')
    if filter_type == 'b':
        print('-'*40)
        month = get_month()
        day = get_day()
        return city, month, day
    elif filter_type == 'm':
        print('-'*40)
        month = get_month()
        return city, month, 'all'
    elif filter_type == 'd':
        print('-'*40)
        day = get_day()
        return city, 'all', day
    else:
        print('-'*40)
        return city, 'all', 'all'


def get_city():
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?').lower()
        if city in [*CITY_DATA]:
            return city
        else:
            print('Incorrect input. Please try again.')


def get_month():
    while True:
        month = input('Which month - January, February, March, April, May, or June?').lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june']:
            return month
        else:
            print('Incorrect input. Please try again.')


def get_day():
    while True:
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            return day
        else:
            print('Incorrect input. Please try again.')


def load_data(city, month, day):
    month = month.lower()
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month # read me
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')
    df['day_of_week'] = df['day_of_week'].str.lower()
    df['hour'] = df['Start Time'].dt.hour # read me
    if(month != 'all'):
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if(day != 'all'):
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_count_df = df['month'].value_counts()
    most_popular_month = str(month_count_df.index[0])
    most_popular_month_count = str(month_count_df.values[0])
    print('Most popular month: ' + most_popular_month + ', Count: ' + most_popular_month_count)

    # TO DO: display the most common day of week
    day_count_df = df['day_of_week'].value_counts()
    most_popular_day = str(day_count_df.index[0])
    most_popular_day_count = str(day_count_df.values[0])
    print('Most popular day: ' + most_popular_day + ', Count: ' + most_popular_day_count)

    # TO DO: display the most common start hour
    hour_count_df = df['hour'].value_counts()
    most_popular_hour = str(hour_count_df.index[0])
    most_popular_hour_count = str(hour_count_df.values[0])
    print('Most popular hour: ' + most_popular_hour + ', Count: ' + most_popular_hour_count)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_s_count_df = df['Start Station'].value_counts()
    most_popular_start_s = str(start_s_count_df.index[0])
    most_popular_start_s_count = str(start_s_count_df.values[0])
    print('Most popular Start Station: ' + most_popular_start_s + ', Count: ' + most_popular_start_s_count)

    # TO DO: display most commonly used end station
    end_s_count_df = df['End Station'].value_counts()
    most_popular_end_s = str(end_s_count_df.index[0])
    most_popular_end_s_count = str(end_s_count_df.values[0])
    print('Most popular End Station: ' + most_popular_end_s + ', Count: ' + most_popular_end_s_count)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    trip_count_df = df['trip'].value_counts()
    most_popular_trip = str(trip_count_df.index[0])
    most_popular_trip_count = str(trip_count_df.values[0])
    print('Most popular trip: ' + most_popular_trip + ', Count: ' + most_popular_trip_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ' + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ' + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count_df = df['User Type'].value_counts()
    print('User Type:')
    print(user_type_count_df.to_string())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count_df = df['Gender'].value_counts()
        print('\nGender:')
        print(gender_count_df.to_string())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year_count_df = df['Birth Year'].value_counts()
        print('\nMost common year of birth: ' + str(int(birth_year_count_df.index[0])))
        birth_year_count_df = birth_year_count_df.sort_index(ascending=False)
        print('Most recent year of birth: ' + str(int(birth_year_count_df.index[0])))
        birth_year_count_df = birth_year_count_df.sort_index(ascending=True)
        print('Earliest year of birth: ' + str(int(birth_year_count_df.index[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data_output(df):
    """Let user view raw data"""

    restart = input('\nWould you like to see raw data? Enter yes or no.\n')
    if restart.lower() == 'yes':
        df = df.drop(columns=['month', 'day_of_week', 'hour', 'trip'])
        df_length = len(df)
        for i in range(0, df_length, 5):
                print(i)
                print(df[i:i+5].to_string())
                restart = input('\nWould you like to see more raw data? Enter yes or no.\n')
                if restart.lower() != 'yes':
                    break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_output(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()




