import requests

class haproxy:
	def __init__(self, url, auth):
		self.url = url
		self.auth = auth

	def enable(self, backend, server):
		return self.post(backend, server, "enable")

	def disable(self, backend, server):
		return self.post(backend, server, "disable")

	def post(self, backend, server, action):
		payload = {'s':server, 'b':backend, 'action':action}
		r = requests.post(self.url, auth=self.auth, data=payload)
		if r.status_code<>200:
			return "Error (%d)" % int(r.status_code)
		return "OK"

	def stats(self):
		r = requests.get("%s;csv" % self.url, auth=self.auth)
		if r.status_code<>200:
			return "Error (%d)" % int(r.status_code)
		lines = r.text.split("\n")[:-1]
		header = lines.pop(0).replace('# ','').strip(",").split(",")
		rows = []
		for l in lines:
			rows.append(dict(zip(header, l.split(","))))
		return rows

	def status(self, backend, server):
		stats = self.stats()
		servers = {}
		for s in stats:
			servers[s['pxname']+':'+s['svname']] = s
		return servers[backend+':'+server] if backend+':'+server in servers else "Not found"
