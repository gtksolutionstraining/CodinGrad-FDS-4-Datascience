"""
This is a Data Science Project
"""
import argparse
from services.files import validate_file_path
from services.data import read_file
from services.profilers.custom import (
    get_features,
    get_info
)
from services.profilers.profileManager import(
    ProfileManager
)
def main(args):
    """Starting point of the Project.

    """
    print("=============================")
    print("Data Science Project")
    print("=============================")
    data_path = args.csv
    status = validate_file_path(data_path)
    if status:
        data = read_file(data_path)
        pm = ProfileManager(data)
        print("Categorical Features: ", pm.num_feats)
        print("Numerical Features: ",pm.cat_feats)
    else:
        print("Provided File doesn't exist")
        print("Please try again later.")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser("Data Science Project Arguments")
    parser.add_argument("-c","--csv",
                        help="Path for CSV File",
                        required=True)
    args = parser.parse_args()
    main(args)