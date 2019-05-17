import os

class Screen(object):
    @classmethod
    def from_json(cls, screen_json, project, api):
        screen = cls(screen_json.get('_id'), project, api)
        screen.name = screen_json.get('name')
        screen.description = screen_json.get('description')
        screen.updated = screen_json.get('updated')
        screen.latest_version_snapshot_url = screen_json.get('latestVersion').get('snapshot').get('url')
        # screen.latest_version_snapshot_id = screen_json.get('latestVersion').get('snapshot').get('_id')
        screen.latest_version_id = screen_json.get('latestVersion').get('_id')

        return screen

    def __init__(self, screen_id, project, api):
        self.id = screen_id
        self.name = None
        self.project = project
        self.description = None
        self.updated = None
        self.latest_version_snapshot_url = None
        # self.latest_version_snapshot_id = None
        self.latest_version_id = None
        self.url = None
        self._api = api

    def get_url(self):
        if not self.url:
            response = self._api._post('urls', data={'url': 'https://app.zeplin.io/project/{}/screen/{}'.format(self.project.id, self.id)})

            self.url = response.json().get('url')
        return self.url
        
    def download(self, filename):
        response = self._api._get(self.latest_version_snapshot_url, build_url=False)
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'wb') as file:
            file.write(response.content)
