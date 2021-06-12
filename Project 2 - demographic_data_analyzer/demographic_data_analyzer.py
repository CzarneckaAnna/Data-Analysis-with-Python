import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
	# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = pd.Series(data=df.race)
    race_count = race.value_counts()

    # What is the average age of men?
    average_age_men = df[df["sex"]=="Male"]["age"].mean()
    average_age_men = float("{:.1f}".format(average_age_men))

    # What is the percentage of people who have a Bachelor's degree?
    education_type = pd.DataFrame(df.education)
    education_type["salary"] = df.salary
    education_type["higher_education"] = 0
    education_type["higher_salary"] = 0

    education_type.loc[education_type.education == "Bachelors", "higher_education"] = 1
    education_type.loc[education_type.education == "Masters", "higher_education"] = 1
    education_type.loc[education_type.education == "Doctorate", "higher_education"] = 1

    education_type.loc[education_type.salary == ">50K", "higher_salary"] = 1

    records_number = education_type["education"].count()
    bachelors_number = education_type[education_type == "Bachelors"]["education"].count()
    percentage_bachelors = (bachelors_number/records_number) * 100
    percentage_bachelors = float("{:.1f}".format(percentage_bachelors))

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`	
    higher_education = education_type[education_type.higher_education == 1]["higher_education"].count()
    lower_education = records_number - higher_education

    # percentage with salary >50K
    high_salary = education_type[education_type.higher_salary == 1]
    
    higher_education_salary = high_salary[high_salary.higher_education == 1]["education"].count()
    lower_education_salary = high_salary[high_salary.higher_education == 0]["education"].count() 

    higher_education_rich = (higher_education_salary / higher_education) * 100
    higher_education_rich = float("{:.1f}".format(higher_education_rich))
    lower_education_rich = (lower_education_salary / lower_education) * 100
    lower_education_rich = float("{:.1f}".format(lower_education_rich))

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    hours_per_week = df[df["hours-per-week"] == 1]

    num_min_workers = hours_per_week["hours-per-week"].count()
    rich_workers = hours_per_week[hours_per_week.salary == ">50K"]["salary"].count()

    rich_percentage = (rich_workers / num_min_workers) * 100
    rich_percentage = int(rich_percentage)

    # What country has the highest percentage of people that earn >50K?
    countries = pd.Series(df[df.salary == ">50K"]["native-country"])
    nbr_people = countries.value_counts()
    
    highest_earning_country = nbr_people.index[0]
    highest_earning_country_percentage = (nbr_people[0] / countries.count()) * 100
    highest_earning_country_percentage = float("{:.1f}".format(highest_earning_country_percentage))

    # Identify the most popular occupation for those who earn >50K in India.
    india_info = df[df["native-country"] == "India"]
    india_info_high_salary = pd.Series(india_info[india_info.salary == ">50K"]["occupation"])
    india_stat = india_info_high_salary.value_counts()
    
    top_IN_occupation = india_stat.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
