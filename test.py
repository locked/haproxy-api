from haproxyapi import haproxy

h = haproxy('http://127.0.0.1:800/', ("admin","admin"))
h.disable("ha", "192.168.0.10")
h.enable("ha", "192.168.0.10")
