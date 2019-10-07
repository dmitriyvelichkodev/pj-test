#!/usr/bin/python

import os
import subprocess

# nginx available in the same containers network by service name in docker-compose: nginx
host = os.getenv('SL_HOST', 'nginx')
port = os.getenv('SL_PORT', 80)
sockets_count = os.getenv('SL_SOCKET_COUNT', 1000)


subprocess.run(["slowloris", "-p {}".format(port), "-s {}".format(sockets_count), host])
