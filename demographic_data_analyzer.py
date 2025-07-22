import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv("adult.data.csv")

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 4. Advanced education (Bachelors, Masters, or Doctorate)
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu = df[df['education'].isin(advanced_education)]
    lower_edu = df[~df['education'].isin(advanced_education)]

    # Percentage with salary >50K
    higher_education_rich = round(
        (higher_edu['salary'] == '>50K').sum() / len(higher_edu) * 100, 1)
    lower_education_rich = round(
        (lower_edu['salary'] == '>50K').sum() / len(lower_edu) * 100, 1)

    # 5. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentage of rich among those who work minimum hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['salary'] == '>50K').sum() / len(min_workers) * 100, 1)

    # 7. Country with highest percentage of rich
    country_stats = df[df['salary'] == '>50K']['native-country'].value_counts() / \
                    df['native-country'].value_counts()
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max() * 100, 1)

    # 8. Most popular occupation for those who earn >50K in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # 📦 Return dictionary
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:",
              higher_education_rich)
        print("Percentage without higher education that earn >50K:",
              lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Percentage of rich among those who work fewest hours:",
              rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:",
              highest_earning_country_percentage)
        print("Top occupations in India for those who earn >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
