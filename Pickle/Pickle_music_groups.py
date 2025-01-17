import pickle
from pickle import HIGHEST_PROTOCOL, Unpickler



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
                return f'Группа {name_of_group}, c альбомами {values[0], values[1]}..... удалена'
        else:
            return f'{name_of_group} :данные для удаления не найдены!!'

    def search(self, data):
        for keys, values in self.music_dict.items():
            if data == keys:
                return f'группа {keys} найдена, её альбомы {values}'
            else:
                for key, values in self.music_dict.items():
                    if data in values:
                        return f'Альбом: {data} найден в группе {key}'
        return f'{data}  :данные не найдены!!'

    def editing(self, data_to_search, *new_data):
        for key, values in self.music_dict.items():
            if key == data_to_search:
                values.append(new_data)
                if len(new_data) == 1:
                    print('у группы:', data_to_search, 'появился новый альбом ', new_data)
                else:
                    print('у группы:', data_to_search, 'появились новые альбомы ', new_data)

                return self.music_dict
        return f'{data_to_search} :такой группы нет в списке'


def save_to_file(name_of_file, data):
    with open(f'{name_of_file}.music', 'wb') as fp:
        pickle.dump(data, fp, HIGHEST_PROTOCOL)
    return f'данные записаны в файл {name_of_file}.music'


class Pickler:

    def __init__(self, protocol=pickle.HIGHEST_PROTOCOL):
        if protocol < 0 or protocol > 5:
            self.protocol = pickle.DEFAULT_PROTOCOL
        elif protocol == 0:
            self.protocol = pickle.HIGHEST_PROTOCOL
        else:
            self.protocol = protocol

    def pickle_data(self, data):
        pickle_data = pickle.dumps(data, self.protocol)
        return pickle_data


class UnPicklerGroups:
    @classmethod
    def unpickle_data(cls, pickle_data):
        unpickled_data = pickle.loads(pickle_data)
        return unpickled_data

    @classmethod
    def load_from_file(cls, name_of_file):
        try:
            with open(name_of_file, 'rb') as fp:
                load_data = pickle.load(fp)
        except FileNotFoundError:
            return 'File Not Found'
        # return f'Данные: {load_data} получены из файла {name_of_file}'
        return load_data


if __name__ == '__main__':
    group = MusicGroupsDict()
    group.add_group('The Beatles', 'Please Please Me (1963)', 'A Hard Days Night (1964)', 'Help! (1965)',
                    'Rubber Soul (1965)Revolver (1966)', 'Sgt. Peppers Lonely Hearts Club Band (1967)',
                    'The Beatles (The White Album) (1968)', 'Abbey Road (1969)')
    # print(group.show())
    group.add_group('The Rolling Stones', 'The Rolling Stones (1964)', 'Aftermath (1966)', 'Beggars Banquet (1968)',
                    'Let It Bleed (1969)', 'Sticky Fingers (1971)', 'Exile on Main St. (1972)', 'Some Girls (1978)')
    # print(group.show())
    # 'Let It Be (1970)'
    group.add_group('The Beatles', 'Let It Be (1970)')
    # print(group.show())
    group.add_group('Pink Floyd', 'The Piper at the Gates of Dawn (1967)', 'The Dark Side of the Moon (1973)',
                    'Wish You Were Here (1975)', 'Animals (1977)', 'The Wall (1979)')
    group.add_group('Nirvana', 'Bleach (1989)', 'Nevermind (1991)')
    print(group.show())
    print(group.delete_data('Pink Floyd'))
    print(group.delete_data('Pinks Floyd'))
    print(group.show())
    print(group.search('A Hard Days Night (1964)'))
    print(group.search('A Hard Days Night (1965)'))
    print(group.search('The Rolling Stones'))
    group.editing('Nirvana', 'In Utero (1993)', 'raka_maka_fo(2025)')
    group.editing('Nirvana', 'In Uteros (1999)')
    print(group.editing('Nirvana', 'In Uteros (1999)'))
    print(group.editing('Nirsvana', 'In Utero (1993)', 'raka_maka_fo(2025)'))
    print(group.show())
    pickle_group = Pickler(5)
    group = pickle_group.pickle_data(group)
    print(group)
    group = UnPicklerGroups.unpickle_data(group)
    print(group)
    print(group.show())
    print(save_to_file('group_list',group))
    group = UnPicklerGroups.load_from_file('group_list.music')
    print(group.show())

