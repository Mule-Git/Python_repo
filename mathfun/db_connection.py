import json


class StudentDB:
    def __init__(self):
        self._data = None

    def connection(self, data_f):
        with open(data_f) as file:
            self._data = json.load(file)

    def get_data(self, s):
        for st in self._data["student"]:
            if st['ID'] == s:
                return st



