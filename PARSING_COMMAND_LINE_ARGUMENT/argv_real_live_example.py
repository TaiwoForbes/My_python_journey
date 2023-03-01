# Run our program as a module with two command line arguments:
# 1. Name of the file to search
# 2. search tearm we are looking for
# Print out all lines containing the search term and the total
# Number of matches

from sys import argv
def read_args():
    """ Check for valid CLI arguments and return them in a dictionary"""
    if len(argv) != 3:
        print("Usage: python -m file.py [file] [keyword]")
        exit()
    return {
        "file_path":argv[1],
        "keyword" : argv[2]
    }
def search_file(file_path: str, keyword: str):
    """Opens & reads file_path returns a list of lines w/ keyword."""
    matches = []
    with open(file_path,"r",encoding="utf8") as f:
        for line in f:
            if keyword in line:
                matches.append(line)

    return matches

def show_results(matches):
    """Get the number of matches/lines and print its length"""
    for line in matches:
        print(line.strip())
    print("Total matches: " + str(len(matches)))
    

args = (read_args())
result = search_file(args['file_path'],args["keyword"])
show_results(result)
