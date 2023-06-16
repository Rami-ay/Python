import pandas as pd

"""
Student Name : Rami Ayoub
Login Name : ramiay
Student ID : 315478966

"""

"""
In this execrsice we wrote a code that reads a CSV file, modifies the data by renaming columns,
converting values, handling missing values, and limiting values in a column,and finally calculates 
and prints the correlation matrix of the modified data.
"""

def data_manipulating():
    #step 1 - uploading the csv file:
    csv_file = pd.read_csv("ex10_file.csv")
    #step 2 - printing the first 7 lines in the csv file:
    print(csv_file.head(7))

    #step 3 - renaming to "Severity":
    csv_file = csv_file.rename(columns={"Severity of illness - worst score during admission": "Severity"})

    #step 4 - keeping only the first word in severity column:
    csv_file['Severity'] = csv_file['Severity'].str.split().str[0]

    #step 5 - changing the severity columns, from words to numbers:
    severity_map = {'Mild': 0, 'Moderate': 1, 'Severe': 2, 'Critical': 3}
    csv_file["Severity"] = csv_file["Severity"].map(severity_map)

    #step 6 - in "Height" column change the Nan to median
    csv_file['Height'].fillna(csv_file['Height'].median(), inplace=True)

    #step 7 - in "Weight" column, delete the Nan rows, and limit
    # the weight to 110:
    csv_file.dropna(subset=['Weight'], inplace=True)

    # Limiting the maximum weight to 110
    csv_file.loc[csv_file['Weight'] > 110, 'Weight'] = 110

    #step 8 - find corelation and print it:
    corr = csv_file.corr()
    print(corr)



"""running the function:"""
data_manipulating()

