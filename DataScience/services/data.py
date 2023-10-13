import pandas as pd
def read_file(data_path):
    """Write comments
    """
    extension = data_path.split(".")[-1]
    if extension == "csv":
        data = pd.read_csv(data_path)
    elif extension == "xlsx" or \
         extension == "xls" or \
         extension == "xlx":
        data = pd.read_excel(data_path)
    return data