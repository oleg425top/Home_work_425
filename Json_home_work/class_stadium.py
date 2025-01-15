import json


class Stadium:
    def __init__(self, name, capacity, year_opened):
        self.name = name
        self.capacity = capacity
        self.year_opened = year_opened

    def display_info(self):
        return f"Name: {self.name}, Capacity: {self.capacity}, Year opened: {self.year_opened}"

    def change_capacity(self, new_capacity):
        self.capacity = new_capacity
        return f"Capacity has been updated to:  {self.capacity} peoples"


class JSONStadiumAdapter:
    @staticmethod
    def to_json(obj):
        if isinstance(obj, Stadium):
            return {'name': obj.name, 'capacity': obj.capacity, 'year opened': obj.year_opened,
                    '<Class>': obj.__class__.__name__,
                    '<Methods>': {'display_info': obj.display_info(), 'change_capacity: ': obj.change_capacity(20000)}}

    @staticmethod
    def from_json(obj):

        try:
            result = Stadium(obj['name'], obj['capacity'], obj['year opened'])
            return result
        except AttributeError:
            print('неверная структура')


if __name__ == '__main__':
    my_stadium = Stadium("Wembley Stadium", 90000, 2007)
    json_stadium = JSONStadiumAdapter.to_json(my_stadium)
    print(json_stadium)
    python_stadium = JSONStadiumAdapter.from_json(json_stadium)
    print(python_stadium.display_info())
    print(python_stadium.change_capacity(120000))
    print(python_stadium.display_info())
    with open(r'stadium.json', 'w', encoding='utf-8') as fh:
        json.dump(my_stadium, fh, default=JSONStadiumAdapter.to_json, ensure_ascii=False, indent=3)
        # fh.write(json_stadium)
    with open(r'stadium.json', 'r', encoding='utf-8') as fh:
        python_stadium = json.load(fh)

    print(python_stadium)
