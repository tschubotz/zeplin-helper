from requests_html import HTMLSession
from .project import Project

class ZeplinAPI(object):

    def __init__(self, username, password, verbose=False):
        self.base_url = 'https://api.zeplin.io'
        self.verbose = verbose

        self._projects = None
        self._projects_dict = {}

        # login
        self._session = HTMLSession()
        login_response = self._post('users/login', {'handle': username, 'password': password})
        self._session.headers['zeplin-token'] = login_response.json().get('token')

    def _build_url(self, path):
        return '{}/{}'.format(self.base_url, path)

    def _post(self, path, data):
        url = self._build_url(path)
        response = self._session.post(url, data=data)

        if self.verbose:
            print('POST {} {}'.format(path, response.status_code))

        return response

    def _get(self, path):
        url = self._build_url(path)
        response = self._session.get(url)

        if self.verbose:
            print('GET {} {}'.format(path, response.status_code))

        return response

    def get_projects(self):
        if not self._projects:
            response = self._get('v2/projects')

            projects = []
            for project_json in response.json().get('projects'):
                project = Project.from_json(project_json, self)
                projects.append(project)
                self._projects_dict[project.id] = project

            self._projects = projects

        return self.projects

    def get_project(self, project_id):
        if not self._projects:
            self.get_projects()
        return self._projects_dict.get(project_id)
