import pandas as pd
import ydata_profiling as yp

class YdataProfiler:
    def __init__(self,data):
        self.data = data
        self.__profile_data()
        self.__get_num_features()
        self.__get_cat_features()

    def __profile_data(self):
        self.report = yp.ProfileReport(self.data)
        self.report = self.report.get_description()

    def __get_num_features(self):
        num_feats = list(map(lambda x:x[0] if x[1]['type'] == 'Numeric' else '',self.report.variables.items()))
        self.num_feats = list(filter(lambda x:x != '',num_feats))

    def __get_cat_features(self):
        cat_feats = list(map(lambda x:x[0] if x[1]['type'] == 'Categorical' else '',self.report.variables.items()))
        self.cat_feats = list(filter(lambda x:x != '',cat_feats))