import pickle

def load_from_file(name_of_file):
    try:
        with open(name_of_file,'rb') as fp:
            load_data = pickle.load(fp)
    except FileNotFoundError:
        return 'File Not Found'
    return f'Данные: {load_data} получены из файла {name_of_file}'

