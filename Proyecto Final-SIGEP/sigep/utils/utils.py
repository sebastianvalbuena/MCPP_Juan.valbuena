import json


class Utils:
    @staticmethod
    def get_codes():
        return json.load(open("resources/codes.json", encoding='utf-8'))

