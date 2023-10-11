"""
This is a Data Science Project
"""
import argparse
from services.files import validate_file_path
from services.data import read_csv
def main(args):
    """Starting point of the Project.

    """
    print("=============================")
    print("Data Science Project")
    print("=============================")
    data_path = args.csv
    status = validate_file_path(data_path)
    if status:
        data = read_csv(data_path)
        print(data)
    else:
        print("Provided File doesn't exist")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser("Data Science Project Arguments")
    parser.add_argument("-c","--csv",
                        help="Path for CSV File",
                        required=False)
    args = parser.parse_args()
    main(args)