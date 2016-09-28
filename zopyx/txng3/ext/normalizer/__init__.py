# placeholder


class Normalizer(object):

    def __init__(self, translation_table= ()):
        self._translation_table = translation_table

    def getTable(self):
        return self._translation_table

    def normalize(self, text):

        for old, new in self._translation_table:
            text = text.replace(old, new)
        return text

