import pandas as pd

class Player():
    def __init__(self, dataframe, start_position):
        self.data = dataframe
        self.position = start_position

    def __init__(self, dataframe, player_name, start_position):
        self.data = dataframe[[dataframe['name'] == player_name]]
        self.position = start_position

    def get_stat(self, stat_name):
        return self.data[stat_name]
