#!/usr/bin/python

import os
import subprocess

# nginx available in the same containers network by service name in docker-compose: server
host = os.getenv('SL_HOST', 'server')
port = os.getenv('SL_PORT', 80)
sockets_count = os.getenv('SL_SOCKET_COUNT', 300)


subprocess.run(["slowloris", "-p {}".format(port), "-s {}".format(sockets_count), host])
