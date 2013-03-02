NameVirtualHost *

<VirtualHost *>

    ServerName sola.protranslate.ru

    DocumentRoot /home/protranslate/sola/www

    LogLevel debug
    ErrorLog /var/log/apache2/sola_errors.log
    CustomLog /var/log/apache2/sola_access.log combined


    Alias /static/ /home/protranslate/sola/static/

    <Location />
        SetHandler uwsgi-handler
        uWSGISocket 127.0.0.1:49153
    </Location>

    <Location ~ /(static|robots\.txt|favicon\.ico)>
        SetHandler None
    </Location>

</VirtualHost>
