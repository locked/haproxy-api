haproxy-api
===========

Python HAProxy API Client


Class Initialization
--------------------

from haproxyapi import haproxy
h = haproxy('http://127.0.0.1:800/', ("user","password"))


Disable/Enable a server on a specific backend
---------------------------------------------

h.disable("backend", "server")
h.enable("backend", "server")

