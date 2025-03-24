# Explore-US-Bikeshare-Data
Explore US Bikeshare Data Project, Udacity's Data Visualization with Microsoft Power BI for ATCI Nanodegree

***

## Description
In this project, you will write Python code to import US bike share data and answer interesting questions about it by computing descriptive statistics. You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics. 

***
## Bike Share Data

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.
The Datasets

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

   - Start Time (e.g., 2017-01-01 00:07:57)
   - End Time (e.g., 2017-01-01 00:20:53)
   - Trip Duration (in seconds - e.g., 776)
   - Start Station (e.g., Broadway & Barry Ave)
   - End Station (e.g., Sedgwick St & North Ave)
   - User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

   - Gender
   - Birth Year

The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them (Chicago, New York City, Washington). These files had more columns and they differed in format in many cases. Some data wrangling has been performed to condense these files to the above core six columns to make your analysis and the evaluation of your Python skills more straightforward.


## Rubric

### Code Quality
| CRITERIA                       | MEETS SPECIFICATIONS                                                       |
| ------------------------------ |----------------------------------------------------------------------------|
|  Functionality of code|  All code cells can be run without error.  |
|  Choice of data types and structures|  Appropriate data types (e.g. strings, floats) and data structures (e.g. lists, dictionaries) are chosen to carry out the required analysis tasks.  |
|  Use of loops and conditional statements|  Loops and conditional statements are used to process the data correctly.  |
|  Use of packages|  Packages are used to carry out advanced tasks.  |
|  Use of functions|  Functions are used to reduce repetitive code.  |
|  Use of good coding practices|  Docstrings, comments, and variable names enable readability of the code.  |

### Script and Questions
| CRITERIA                       | MEETS SPECIFICATIONS                                                       |
| ------------------------------ |----------------------------------------------------------------------------|
|  Solicit and handle raw user input  |  Raw input is solicited and handled correctly to guide the interactive question-answering experience; no errors are thrown when unexpected input is entered. <br><Br> User inputs should be made case insensitive, which means the input should accept the string of "Chicago" and its case variants, such as "chicago", "CHICAGO", or "cHicAgo". <Br><Br> You should also implement error handlings so your program does not throw any errors due to invalid inputs. For example, if the user enters "Los Angeles" for the city, the error handling should reject the user input and avoid breaking the codes.|
|  Use descriptive statistics to answer questions about the data. Raw data is displayed upon request by the user.  |  Descriptive statistics are correctly computed and used to answer the questions posed about the data. Raw data is displayed upon request by the user in this manner: Script should prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'.  |

***

## Statistics Computed

You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

1. Popular times of travel (i.e., occurs most often in the start time)

   - most common month
   - most common day of week
   - most common hour of day

2. Popular stations and trip

   - most common start station
   - most common end station
   - most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration

   - total travel time
   - average travel time

4. User info

   - counts of each user type
   - counts of each gender (only available for NYC and Chicago)
   - earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Project files
- **bikeshare.py** - Executable Python Project File
- **chicago.zip** - Dataset used for analysis (zipped csv file)
- **new_york_city.zip** - Dataset used for analysis (zipped csv file)
- **washington.zip** - Dataset used for analysis (zipped csv file)
***

## Disclaimer

Data and project information were kindly provided by [Udacity](https://www.udacity.com/).
