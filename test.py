from haproxyapi import haproxy
import pprint

h = haproxy('http://127.0.0.1:800/', ("admin","admin"))

print h.disable("ha", "192.168.0.10")
print h.enable("ha", "192.168.0.10")

stats = h.stats()
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(stats)
#print stats
for s in stats:
	print "[" + s['pxname'] + "] " + s['svname'] + ' : ' + s['status']

print h.status("ha", "192.168.0.10")
