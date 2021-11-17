server {
    listen 8000;
    server_name 127.0.0.1;

    #access_log /var/log/nginx/codejob.co.kr_access.log;
    #error_log /var/log/nginx/codejob.co.kr_error.log;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        #alias /home/shkim/pyBook/ch9/www_dir/static/;
        root /home/shkim/pyBook/ch9/www_dir;
    }

    location / {
        include /home/shkim/pyBook/ch9/www_dir/uwsgi_params;
        uwsgi_pass 127.0.0.1:8001;
        #uwsgi_pass unix:///home/shkim/pyBook/ch9/www_dir/ch9.sock;
    }
}

