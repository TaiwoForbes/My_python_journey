import csv

# Using a function
def write_csv(data,path):
    with open(path,"w") as csv_file:
        # Specifying the mode of the file, read or write. In this case,write.
        writer = csv.writer(csv_file, delimiter=",")
        for line in data:
            # Writing our data row by row
            writer.writerow(line)
if __name__ == "__main__": 

    """
    data = our list that we want to write.
    Split it so we get a list of lists.
    """

    data = [
            "first_name,last_name,age".split(","),
            "John,Doe,22".split(","),
            "Jane,Doe,31".split(","),
            "Jack,Reacher,27".split(",")
            ]
    path = "file.csv"
    file = write_csv(data,path)
    print(file)

# READING FROM A FILE

with open("class.csv") as f:
    read = csv.reader(f)
    for row in read:
        print(read)





