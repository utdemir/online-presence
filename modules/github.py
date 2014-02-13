import requests

class GitHubBase:
    API_URL = "https://api.github.com"

class GitHub(GitHubBase):
    def __init__(self, username, password=None):
        self._username = username
        self._password = password
        self._d = None

    def refresh(self):
        self._d = self._json(self.API_URL + "/users/%s" % self._username)
        if self._d == None:
            raise ValueError

    def __getitem__(self, name):
        if not self._d: 
            self.refresh()
        
        req = None
        if name.endswith("_json"): req = self._d[name[:-5] + "_url"]
        elif name == "json": req = self._d["url"]
        if req: 
            ret = self._json(req)
            self._d[name] = ret

        return self._itemize(self._d[name])
    
    def _itemize(self, obj):
        if isinstance(obj, dict):
            return GitHubItem(self._username, self._password, obj)
        elif isinstance(obj, list):
            return list(map(self._itemize, obj))
        else:
            return obj

    def _json(self, url):
        auth = (self._username, self._password) if self._password else None 
        try:
            return requests.get(url, auth=auth).json()
        except requests.exceptions.RequestException:
            return None

class GitHubItem(GitHub):
    def __init__(self, username, password, d):
        super().__init__(username, password)
        self._d = d

    def __repr__(self):
        return repr(self._d)

MAIN = GitHub
