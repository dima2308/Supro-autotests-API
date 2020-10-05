import requests


class Client:
    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

    def get_independent_offers(self, data: dict):
        return self._s.post(self.host + "/get-independent-offers", json=data)

    def get_dependent_offers(self, data: dict):
        return self._s.post(self.host + "/get-dependent-offers", json=data)

    def get_active_banners(self):
        return self._s.get(self.host + "/get-active-banners")

    def get_version(self):
        return self._s.get(self.host + "/get-version")

    def register_sale(self, data: dict):
        return self._s.post(self.host + "/register-sale", json=data)

    def get_personal_offers(self, data: dict):
        return self._s.post(self.host + "/get-personal-offers", json=data)
