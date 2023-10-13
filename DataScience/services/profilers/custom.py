import pandas as pd
def get_features(data:pd.DataFrame):
    features = data.columns.to_list()
    return features

def get_info(data:pd.DataFrame):
    info = data.info()
    return info