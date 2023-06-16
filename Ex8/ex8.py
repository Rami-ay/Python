import re

"""
Student Name : Rami Ayoub
Login Name : ramiay
Student ID : 315478966

"""

"""
Ex1: in this exercise we got two files , txt file that contains cities and their location
including coordinations of the largest 30 cities in USA and a csv that contains multiple 
Postal codes for each city and we print the city and it's postal code to the screen.

Ex2: in this exercise we got a run log report that contains information of multiple runs
we run over the given report and extract the successful runs to an output txt file.
"""


def seperate_city_state_name(lst):
    """function that runs over a list and corrects the names that has
    a capital letter immeditly after a small letter:"""
    try:
        for index1, x in enumerate(lst):
            for index2, y in enumerate(x):
                if y.islower() and index2 + 1 < len(x) and x[index2 + 1].isupper():
                    lst[index1] = lst[index1][0:index2 + 1]
    except TypeError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


""" EX1 :"""

def print_largest_city_postal_codes(txt_file_path, csv_file_path):
    """
    This function reads two given files , txt file that contains the largest 30
    cities names and their cooardination.
    the second file is csv file that contain postal codes of these cities.
    if one city has multiple zip code we take the first one.

    the output is printed on the screen:
    each city and it's postal code.
    """

    temp_list = []
    # dict to store city and postal code pairs
    city_postal_codes = {}

    try:
        # read the txt file
        with open(txt_file_path, 'r') as cities_file:
            # skip the titles line
            next(cities_file)
            for line in cities_file:
                # split each line by tabs
                columns = line.strip().split('\t')
                # extract city name
                city = re.sub(r'\[.*\]', '', columns[1]).strip()
                temp_list.append(city)

            # run over the list and clean the city names:
            seperate_city_state_name(temp_list)
            # this line is becouse we didn't succedd to start from second line:
            temp_list = temp_list[1:]
            # now we have clear names we add to dict:
            for clear_city in temp_list:
                city_postal_codes[clear_city] = ''

    except FileNotFoundError:
        print("Error: File not found.")
        return

    try:
        # read the .csv file
        with open(csv_file_path, 'r') as postal_codes_file:
            # skip the titles line
            next(postal_codes_file)
            for line in postal_codes_file:
                # use regex to get postal code and city
                match = re.match(r"(\d+),([\w'?/?\-?\s]{0,})(,[\w'?/?\-?\s]{0,}),", line)
                if match:
                    postal_code = match.group(1)
                    city = match.group(2).strip()
                    if city in city_postal_codes and not city_postal_codes[city]:
                        city_postal_codes[city] = postal_code

    except FileNotFoundError:
        print("Error: File not found.")
        return

    # print the postal codes
    for city, postal_code in city_postal_codes.items():
        print(f"{city} {postal_code}")

    cities_file.close()
    postal_codes_file.close()


"""EX2:"""


def store_successful_runs(run_log):
    """This code stores successful runs from given run log file by
      writing into an output file."""

    try:
        # open file to store the successful runs in it:
        with open("output.txt", "w") as output_file:
            successful_runs = []
            # open the file and read the report:
            with open(run_log, 'r') as runs_file:
                lines = runs_file.readlines()
                """ we want to store the line that does not contain the words:
                "ERROR", "UNDERFLOW", "DID NOT CONVERGE":"""
                for line in lines:
                    if not any(keyword in line for keyword in ["ERROR", "UNDERFLOW", "DID NOT CONVERGE"]):
                        # add the lines that succeeded to a list:
                        successful_runs.append(line)

                for run in successful_runs:
                    # Find the number and the file name and write to new file
                    match = re.search(r"RUN(\s\d*\s)COMPLETED. OUTPUT IN FILE (\w*.\w*).", run)
                    if match:
                        output_file.write(match.group(1) + match.group(2) + "\n")

    except FileNotFoundError:
        print("Error: File not found.")


while (True):
    ex_num = (input("Please Enter The Exercise Number (1/2) or 'exit': "))
    if (ex_num == '1'):
        print_largest_city_postal_codes("2022_largest_cities.txt", "us_postal_codes.csv")
    elif (ex_num == '2'):
        account = store_successful_runs("atoms2.log")
    elif (ex_num == 'exit'):
        break
    else:
        print("Exercise Number is Not Valid, Try Again!")
