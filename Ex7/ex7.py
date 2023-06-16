"""
Student Name : Rami Ayoub
Login Name : ramiay
Student ID : 315478966

"""

"""
In this exercise we get an sql file that contains tables in a given format
and we convert each table and its content to .csv file of a format given to
us too.
Including error handling
Note: we did not succed to make the read_sql_file function to be a generator
so the code directly makes all the csv file and does not support the next function.
"""

def read_sql_file(file_path):
    """the main function that converts sql to csv's"""
    try:
        # Open thesql file
        with open(file_path, 'r') as file:
            # Init variables
            out_csv_file = None
            csv_name = None
            columns = None

            # keep taking lines
            for line in file:
                if line.startswith("CREATE TABLE"):
                    #string to hold the first line in csv:
                    columns = ""
                    #while the table scope not closed:
                    while file.read(1) != ")":
                        # turn into a list
                        split_line = file.readline().split(" ")
                        # throw the space
                        split_line = split_line[1:]
                        if is_needed_title(split_line[0]):
                            columns += table_name(split_line) + ","
                            # delete the last char
                    columns = columns[:-1]
                # now if we have INSERT INTO:
                if "INSERT INTO" in line:
                    csv_name = create_csv(line.split(" "))
                    try:
                        with open(csv_name, "w") as out_csv_file:
                            write_2csv(out_csv_file, line, columns)
                    except FileExistsError:
                        print(f"CSV file '{csv_name}' already exists.")
                    except Exception as e:
                        print(f"Error writing to CSV file '{csv_name}': {str(e)}")
                        raise


    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file '{file_path}': {str(e)}")
        raise
    finally:
        # Close files
        if file:
            file.close()
        if out_csv_file:
            out_csv_file.close()


def create_csv(line_list):
    """ Make the table name and add csv"""
    table_name = line_list[2]
    if table_name.startswith("`") and table_name.endswith("`"):
        table_name = table_name[1:-1]
    csv_file_name = table_name + ".csv"
    return csv_file_name

def write_2csv(csv_file, line,columns):
    """ When we find INSERT INFO we want to save the content """
    # write the titles to the file
    csv_file.write(columns + '\n')
    information = line.split("),(")
    information[0] = information[0].split("(")[1]
    information[-1] = information[-1].replace(");\n", "")

    for ifo in information:
        csv_file.write(ifo + '\n')


def table_name(tempLine):
    """ return the first cell in the list without ' ' """
    first_cell = tempLine[0].strip()
    return first_cell


def is_needed_title(str):
    """return true if it is the needed title, false o.w
     needed title will be between ' ' """
    return str[0] == "`" and str[len(str) -1] == "`"




read_sql_file("demo.sql")