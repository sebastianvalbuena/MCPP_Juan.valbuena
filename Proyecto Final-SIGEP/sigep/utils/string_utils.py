import re

import unidecode


class StringUtils:
    @staticmethod
    def get_monospaced_text(text):
        return re.sub(' +', ' ', text)

    @staticmethod
    def get_titled_text(text):
        return text.title()

    @staticmethod
    def get_no_accent_text(text):
        return unidecode.unidecode(text)

    @staticmethod
    def get_text_without_digits(text):
        text = re.sub('\\d+C?', '', text)
        return re.sub('Ii*', '', text)

    @staticmethod
    def get_text_without_dashes(text):
        return re.sub('-(.*)-', '', text)
