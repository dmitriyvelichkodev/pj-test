## setup

Currently docker-compose allows to start server(nginx) and client(slowloris) with command:

`docker-compose up --scale client=NUMBER_OF_INSTANCES`

NUMBER_OF_INSTANCES: scale for container with python based slowloris client.
Nginx container will be available inside docker network by the hostname: server

You can specify host, port and number of socket to open from one container with env variables in docker-compose.yml
```
SL_HOST - host
SL_PORT - port
SL_SOCKET_COUNT - sockets_count
```

### client (slowloris)
Container uses [slowloris](https://github.com/gkbrk/slowloris) python package

### server (nginx)
Configs to protect from ddos:
- limited number of connections per ip: `10`
- rate-limited requests to: `5req/s`
- extended worker connection limit: `100000`
- setup prevention for slow connection throttle
    ```
    reset_timedout_connection on;
    client_body_timeout 10;
    client_header_timeout 10;
    send_timeout 2;
    keepalive_timeout  30; 
    ```
Container provides already proper configs for nginx process and user:
- system open file limit
  ```
  cat /proc/sys/fs/file-max
  524288
  ```
- user open file limit - user is nginx
 ```
    ulimit -Hn
    1048576
    ulimit -Sn
    1048576
  ```
- open files for nginx process limit
 
    `Max open files            1048576              1048576              files`
