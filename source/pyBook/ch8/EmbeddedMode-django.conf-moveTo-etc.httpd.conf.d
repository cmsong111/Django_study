# for mod_wsgi and django by shkim
#
# ~/ch8/mysite project - embedded mode

WSGIScriptAlias / /home/shkim/pyBook/ch8/mysite/wsgi.py
WSGIPythonHome /home/shkim/VENV/v3PyBook
WSGIPythonPath /home/shkim/pyBook/ch8

<Directory /home/shkim/pyBook/ch8/mysite>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

Alias /static/ /home/shkim/pyBook/ch8/www_dir/static/
<Directory /home/shkim/pyBook/ch8/www_dir/static>
Require all granted
</Directory>
