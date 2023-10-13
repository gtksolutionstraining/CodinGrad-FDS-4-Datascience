from services.profilers.ydata import YdataProfiler
class ProfileManager:
    def __init__(self,data):
        self.data = data
        self.ydata = YdataProfiler(data)
        self.__get_num_features()
        self.__get_cat_features()

    def __get_num_features(self):
        self.num_feats = self.ydata.num_feats
    
    def __get_cat_features(self):
        self.cat_feats = self.ydata.cat_feats