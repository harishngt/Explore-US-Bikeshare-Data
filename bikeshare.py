import time
import pandas as pd
import numpy as np

"""Purpose: Use Python, Pandas, NumPy, to explore US bikeshare data for three cities (Chicago, New York, and Washington) 
    
    by Harish
    Project: Explore US Bikeshare Data
    Due Date: March 25, 2025
    Cohort: March 2025 - Data Visualization with Microsoft Power BI for ATCI Nanodegree from Udacity
"""
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print("Greetings! Let's explore some US bikeshare data!")
    
    # Get user input for city (chicago, new york, washington). Use a while loop to handle invalid inputs.
    while True:
        city =input("Enter the City Name (Chicago, New York,or Washington): \n").lower()
        if city in cities:
            break
        else:
            print('Invalid city! Please enter Chicago, New York, or Washington')
            
    # Get user to filter by month, day, or none.
    
    while True:
        filter_type = input("Would you like to filter by Month, Day, or None? ").strip().lower()
        if filter_type in ["month", "day", "none"]:
            break
        print("Invalid input! Please enter 'month', 'day', or 'none'.")

    month, day = "all", "all"  # Default values

    filters = {"month": months, "day": days}

    if filter_type in filters:
        while True:
            filter_input = input(f"Enter {filter_type} or 'all': ").strip().lower()
            if filter_input in filters[filter_type]:
                if filter_type == "month":
                    month = filter_input
                else:
                    day = filter_input
                break
            print(f"Invalid {filter_type}! Enter a valid {filter_type} or 'all'.")

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
    
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all': 
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Popular Times of Travel...\n')
    start_time = time.time()

    # Extract most common month, day, and hour
    popular_month = months[df['month'].mode()[0] - 1]  # Convert index to month name
    print('Most Common Month:', popular_month.capitalize())

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day of the Week:', popular_day)

    popular_hour = df['Start Time'].dt.hour.mode()[0]
    formatted_hour = f"{popular_hour % 12 or 12} {'AM' if popular_hour < 12 else 'PM'}"
    print('Most Common Start Hour:', formatted_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("Most Common Start Station:", df['Start Station'].mode()[0]) # Displays most common start station
    print("Most Common End Station:", df['End Station'].mode()[0])  # Displays most end start station
    print("Most Common Trip:", (df['Start Station'] + " to " + df['End Station']).mode()[0])    # Displays most common trip
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Display total travel time
    def format_duration(seconds):
        return time.strftime("%H Hours, %M Minutes, %S Seconds", time.gmtime(seconds))

    total_duration = df['Trip Duration'].sum()
    average_duration = df['Trip Duration'].mean()

    
    print(f"Total Travel Time: {format_duration(total_duration)}")
    # Display mean travel time
    print(f"Average Travel Time: {format_duration(average_duration)}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of Each User Type:\n", df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:
        print("\nCounts of Each User Gender:\n", df['Gender'].value_counts())
    else:
        print(f"No gender data available for {city.title()}.")

    # Display birth year statistics
    if 'Birth Year' in df.columns:
        print("\nBirth Year Stats")
        print(f"Oldest User: {int(df['Birth Year'].min())}")
        print(f"Youngest User: {int(df['Birth Year'].max())}")
        print(f"Most Common Birth Year: {int(df['Birth Year'].mode()[0])}")
    else:
        print(f"No birth year data available for {city.title()}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual_data(df):
    # Ask user if they want to see individual trip data.
    start_data = 0
    while start_data < len(df):
        raw_data = input("\nWould you like to see individual trip data? Enter 'yes' or 'no'.\n").lower()
        if raw_data != 'yes':
            break
        print(df.iloc[start_data:start_data + 5])
        start_data += 5
                    
def main():
    while True:
        city, month, day = get_filters()
        print("You selected {}, {}, and {}.".format(city.title(), month.title(), day.title()))
        
        df = load_data(city, month, day)
        #print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        individual_data(df)

        if input("\nWould you like to restart? Enter yes or no.\n").lower() != 'yes':
            break

if __name__ == "__main__":
	main()