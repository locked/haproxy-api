import requests

class haproxy:
	def __init__(self, url, auth):
		self.url = url
		self.auth = auth

	def enable(self, backend, server):
		self.post(backend, server, "enable")

	def disable(self, backend, server):
		self.post(backend, server, "disable")

	def post(self, backend, server, action):
		payload = {'s':server, 'b':backend, 'action':action}
		r = requests.post(self.url, auth=self.auth, data=payload)
