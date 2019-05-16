from .screen import Screen
from .section import Section

class Project(object):
    @classmethod
    def from_json(cls, project_json, api):
        project = cls(project_json.get('_id'), api)
        project.name = project_json.get('name')
        project.status = project_json.get('status')
        project.type = project_json.get('type')
        project.created = project_json.get('created')
        project.updated = project_json.get('updated')
        project.density = project_json.get('density')
        # ignore icon
        project.thumbnail = project_json.get('thumbnail')
        # ignore extensions
        # ignore users
        return project

    def __init__(self, project_id, api):
        self.id = project_id
        self.name = None
        self.status = None
        self.type = None
        self.created = None
        self.updated = None
        self.density = None
        self._api = api

        self._screens = []
        self._screens_dict = {}

        self._sections = []
        self._sections_dict = {}

    def get_screens(self):
        if not self._screens:
            response = self._api._get('v2/projects/{}'.format(self.id))
            
            project_json = response.json()

            # update the project
            self.name = project_json.get('name')
            self.type = project_json.get('type')
            self.created = project_json.get('created')
            self.updated = project_json.get('updated')

            # fetch screens
            for screen_json in response.json().get('screens'):
                screen = Screen.from_json(screen_json, self, self._api)
                self._screens.append(screen)
                self._screens_dict[screen.id] = screen

            # # fetch sections
            # for section_json in response.json().get('sections'):
            #     section = Section.from_json(section_json, self._api)
            #     for screen_id in section_json.get('screens'):
            #         screen = self.get_screen(screen_id)
            #         section._screens.append(screen)
            #         section._screens_dict[screen_id] = screen
            #     self._sections.append(section)
            #     self._sections_dict[section.id] = section

        return self._screens

    def get_screen(self, screen_id):
        if not self._screens:
            self.get_screens()
        
        # s = self._screens_dict.get(screen_id)
        # response = self._api._get('v3/projects/{}/screens/{}/versions/{}/snapshot'.format(self.id, s.id, s.latest_version_id))
        # response = self._api._session.get(response.json().get('snapshot'))
        return self._screens_dict.get(screen_id)