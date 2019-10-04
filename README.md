# client


## server (nginx)
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
