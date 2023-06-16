import pandas as pd
import numpy as np
from datetime import date
import datetime as dt
import matplotlib.pyplot as plt

"""
Student Name : Rami Ayoub
Login Name : ramiay
Student ID : 315478966

"""

"""
The code performs data analysis on a CSV file.
It includes steps such as reading the file, data manipulation, ploting...etc
we did catogrization, added columns and plotted two plots using pandas and matplotlib
following the given instructions in the exercise
"""
def LowMidHig(total_purchases):
    """This function categorizes the total number of purchases
    into "Low", "Mid", or "High" based on predefined thresholds."""

    if total_purchases < 10:
        return "Low"
    elif total_purchases >= 10 and total_purchases <= 20:
        return "Mid"
    else:
        return "High"



def map_educational_level(df):
    """This function maps the values in the "educational_level" column
     of a DataFrame to corresponding numeric values based on a predefined mapping dictionary."""

    edu_mapping = {
        "Basic": 0,
        "High School": 1,
        "Graduation": 2,
        "Master": 3,
        "PhD": 4
    }
    df["educational_level"] = df["educational_level"].map(edu_mapping)


def plot_educational_level(df):
    """This function plots the relationship between educational level
     and two variables: annual income and total purchases."""

    df = df.sort_values(by="educational_level", ascending=True)

    # Creating the subplot for educational_level by annual_income:
    plt.subplot(1, 2, 1)
    plt.title("educational_level by annual_income")
    plt.ylabel("annual_income")
    plt.plot(df['educational_level'], df['annual_income'], color='b')

    # Creating the subplot for educational_level by total_purchases:
    plt.subplot(1, 2, 2)
    plt.title("educational_level by total_purchases")
    plt.ylabel("total_purchases")
    plt.plot(df['educational_level'], df['total_purchases'], color='r')
    plt.show()

def data_analysis():
    # step 1 - uploading the csv file:
    csv_file = pd.read_csv("project_data.csv")

    # Step 2 - sing unique() function on the "marital_status" column and printing the values:
    unique_marital_status = csv_file["marital_status"].unique()
    print(unique_marital_status)

    # Step 3 - replacing "widow" with "Widowed" in  csv_file:
    csv_file["marital_status"].replace("Widow", "Widowed", inplace=True)

    # Step 4 - Using value_counts() function on the "educational_level" column with normalize=True:
    csv_file["educational_level"].replace(csv_file["educational_level"].value_counts(normalize=True), inplace=True)

    # Step 5 - filter and sort "Singles":
    singles_data = csv_file.loc[csv_file["marital_status"].isin(["Single"])]
    singles_sorted = singles_data.sort_values(by="annual_income", ascending=False)

    print(singles_sorted)

    # Step 6 - add a new column for the sum of online_purchases and store_purchases:
    csv_file["total_purchases"] = csv_file["online_purchases"] + csv_file["store_purchases"]

    # Step 7 - add a new column for categorizing total_purchases:
    csv_file["purchase_category"] = csv_file["total_purchases"].apply(LowMidHig)

    #Step 8 - Pie chart of the purchase_category:
    purchase_counts = csv_file["purchase_category"].value_counts()  # Count the occurrences of each category
    purchase_counts.plot(kind="pie", autopct='%1.1f%%')  # Create a pie chart with percentage values
    plt.axis('equal')  # Set the aspect ratio to make the pie chart circular
    plt.legend()  # Display the legend
    plt.show()  # Show the pie chart

    # Step 9 - grouping by "purchase_category" and calculating averages and sums of purchases:
    grouped_purchases = pd.DataFrame(csv_file.groupby(by='purchase_category')
                                  [['annual_income', 'online_purchases']].mean()).reset_index()
    print(grouped_purchases)

    # Step 10 - plot educational_level by annual_income and total_purchases:
    med = csv_file["annual_income"].median()
    csv_file["annual_income"].fillna(med, inplace=True)
    # Map educational_level to numeric values
    map_educational_level(csv_file)
    # Plot educational_level by annual_income and total_purchases
    plot_educational_level(csv_file)



"""running the function:"""
data_analysis()