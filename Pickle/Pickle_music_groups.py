import pickle

def load_from_file(name_of_file):
    try:
        with open(name_of_file,'rb') as fp:
            load_data = pickle.load(fp)
    except FileNotFoundError:
        return 'File Not Found'
    return f'Данные: {load_data} получены из файла {name_of_file}'

class MusicGroupsDict:
    def __init__(self):
        self.music_dict = {}

    def add_group(self, group, *albums):
        if group in self.music_dict.keys():
            self.music_dict[group].append(albums)
        else:
            self.music_dict.update({group: albums})
