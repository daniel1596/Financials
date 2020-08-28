class DictionaryToObjectConverter:
    """
    This class maps dictionary items to properties of an object.
    This with IDE auto-completion: one can access item.prop instead of item["prop"].
    If needing this to make this fancier, e.g. for nested dictionary data, see https://stackoverflow.com/a/1305682
    """
    def __init__(self, dictionary: dict):
        for k, v in dictionary.items():
            setattr(self, k, v)