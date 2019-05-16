class Section(object):
    @classmethod
    def from_json(cls, section_json, api):
        section = cls(section_json.get('_id'), api)
        section.name = section_json.get('name')
        return section

    def __init__(self, section_id, api):
        self.id = section_id
        self.name = None
        self._screens = []
        self._screens_dict = {}

        self._api = api
