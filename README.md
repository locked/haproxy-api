haproxy-api
===========

Python HAProxy API Client


Requirements
------------

- requests >=0.12 (http://docs.python-requests.org/en/latest/)


Class Initialization
--------------------

```
from haproxyapi import haproxy
h = haproxy('http://127.0.0.1:800/', ("user","password"))
```


Disable/Enable a server on a specific backend
---------------------------------------------

```
h.disable("backend", "server")
h.enable("backend", "server")
```


Display Statistics
------------------

```
print h.stats()
```

Or retrieve a specific server status:

```
print h.status("backend", "server")
```
