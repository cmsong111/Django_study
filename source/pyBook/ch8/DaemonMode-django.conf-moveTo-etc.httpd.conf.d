# for mod_wsgi and django by shkim
#
# ~/ch8/mysite project - daemon mode

WSGIScriptAlias / /home/shkim/pyBook/ch8/mysite/wsgi.py
WSGIDaemonProcess mygroup python-home=/home/shkim/VENV/v3PyBook python-path=/home/shkim/pyBook/ch8
WSGIProcessGroup mygroup

<Directory /home/shkim/pyBook/ch8/mysite>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

Alias /static/ /home/shkim/pyBook/ch8/www_dir/static/
<Directory /home/shkim/pyBook/ch8/www_dir/static>
Require all granted
</Directory>
