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

    def add_group(self, groups, *albums):
        if groups in self.music_dict.keys():
            self.music_dict[groups].append(albums)
        else:
            self.music_dict.update({groups: list(albums)})
        return f'{groups}, {albums} :данные добавлены'
    def show(self):
        return self.music_dict

    def delete_data(self, name_of_group):
        for keys, values in self.music_dict.items():
            if name_of_group == keys:
                self.music_dict.pop(keys)
                return f'Группа {name_of_group}, c альбомами {values} удалена'
        else:
            return f'{name_of_group} :данные для удаления не найдены!!'

if __name__ == '__main__':
    group =MusicGroupsDict()
    group.add_group('The Beatles', 'Please Please Me (1963)','A Hard Days Night (1964)','Help! (1965)','Rubber Soul (1965)Revolver (1966)','Sgt. Peppers Lonely Hearts Club Band (1967)','The Beatles (The White Album) (1968)','Abbey Road (1969)')
    # print(group.show())
    group.add_group('The Rolling Stones','The Rolling Stones (1964)', 'Aftermath (1966)', 'Beggars Banquet (1968)', 'Let It Bleed (1969)', 'Sticky Fingers (1971)', 'Exile on Main St. (1972)', 'Some Girls (1978)')
    # print(group.show())
    #'Let It Be (1970)'
    group.add_group('The Beatles', 'Let It Be (1970)')
    # print(group.show())
    group.add_group('Pink Floyd', 'The Piper at the Gates of Dawn (1967)','The Dark Side of the Moon (1973)', 'Wish You Were Here (1975)', 'Animals (1977)', 'The Wall (1979)')
    print(group.show())
    print(group.delete_data('Pink Floyd'))
    print(group.delete_data('Pinks Floyd'))
    print(group.show())





