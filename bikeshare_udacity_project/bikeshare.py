import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all','jan', 'feb', 'march', 'abril', 'may', 'june']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities = ['chicago','new york city', 'washington']
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('from which city you want to get the data?(chicago,new york city, washington)\n').lower()
    while True:
        if city in cities:
            break
        else:
            city = input('please enter the city correctly (chicago,new york city, washington)\n').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('from which city you want to get the data?(all,jan, feb, march, abril, may, june)\n').lower()
    while True:
        if month in months:
            break
        else:
            month = input('please enter the month correctly (all,jan, feb, march, abril, may, june)\n').lower()
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    day = input('from which city you want to get the data?(all, saturday, sunday, monday, tuesday, wednesday, thursday, friday)\n').lower()
    while True:
        if day in days:
            break
        else:
            day = input('please enter the day correctly (all, saturday, sunday, monday, tuesday, wednesday, thursday, friday)\n').lower()
    

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
    # making sub Series to use later
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    

    first5rows = input('do you want to see the first 5 rows of the data?yes or no?').lower()
    x = 5
    while True:
        if first5rows == 'yes' or first5rows == 'no':
            break
        else:
            first5rows = input('please type yes or no?').lower()
    while first5rows == 'yes':
        print(df[x-5:x])
        first5rows = input('do you want to see the next 5 rows of the data?yes or no?').lower()
        if first5rows == 'no':
            break
        elif first5rows != 'yes':
            first5rows = input('please type yes or no?').lower()
        x += 5
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['comp'] = df['Start Station'] + '---->' + df['End Station']
    if month != 'all':
        month = months.index(month)
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_freq = df['month'].mode()[0]
    print('\nthe most common month is : ', months[month_freq]) 
    # TO DO: display the most common day of week
    day_freq = df['day'].mode()[0]
    print('the most common day is : ', day_freq) 
    # TO DO: display the most common start hour
    hr_freq = df['hour'].mode()[0]
    print('the most common hour is : ', hr_freq) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# NEW FUNCTION
def least_users(df):
    '''Displays the minimum users per hour, day or month'''
    print('\nCalculating The Least Frequent Times of Travel...\n')
    start_time = time.time()

    #getting the least frequent 3 months
    month_freq = df['month'].value_counts().index[-3:]
    ## https://stackoverflow.com/questions/49966675/pandas-least-frequent-value-in-column
    print('the least 3 number of user in monthes is in : ',months[month_freq[0]],', ', months[month_freq[1]], ', ', months[month_freq[2]]) 
    #getting the least frequent 3 days
    day_freq = df['day'].value_counts().index[-3:]
    print('the least 3 number of user in days is in : ', day_freq[0], ', ', day_freq[1], ', ', day_freq[2]) 
    #getting the least frequent 3 hours
    hr_freq = df['hour'].value_counts().index[-3:]
    print('the least 3 number of user in hours is in : ', hr_freq[0], ', ', hr_freq[1], ', ', hr_freq[2]) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    startstation_freq = df['Start Station'].mode()[0]
    print('\nthe most common start station is : ', startstation_freq)
    
    # TO DO: display most commonly used end station
    endstation_freq = df['End Station'].mode()[0]
    print('the most common end station is : ', endstation_freq)

    # TO DO: display most frequent combination of start station and end station trip
    startendstation_freq = df['comp'].mode()[0]
    print('the most common start---->end station is : ', startendstation_freq)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Difference'] = df['End Time'].sub(df['Start Time'], axis=0)
    ## https://stackoverflow.com/questions/37840812/pandas-subtracting-two-date-columns-and-the-result-being-an-integer
    print('\nthe total travel time : ',df['Difference'].sum()) 

    # TO DO: display mean travel time
    print('the mean travel time : ', df['Difference'].mean()) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nthe types and numbers of users is \n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        user_Gen = df['Gender'].value_counts()
        print('\nthe number of each gender is \n',user_Gen)
    else:
        print('gender is not provided in this data')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birthye = df['Birth Year'].min()
        birthyr = df['Birth Year'].max()
        birthyc = df['Birth Year'].mode()[0]
        print('\nthe earliest birth year is : ', birthye)
        print('\nthe most recent birth year is : ', birthyr)
        print('\nthe common birth year is : ', birthyc)
    else:
        print('birth year is not provided in this data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        least_users(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
