<VirtualHost *:80>

    ServerName twittertickets.com
    ServerAdmin phawksworth@gmail.com
  
    LogLevel warn
    ErrorLog /var/log/apache2/twittertickets.com.error.log
    CustomLog /var/log/apache2/unobtrusify.com.access.log combined
    LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i \" \"%{Cookie}i\""

    <Directory /var/www/twittertickets.com>
        Order deny,allow
        Allow from all
    </Directory>
    
    DocumentRoot /var/www/twittertickets.com/

</VirtualHost>