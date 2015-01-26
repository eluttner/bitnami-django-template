##Django config files

https://wiki.bitnami.com/Components/Django

Search for django on /opt/bitnami/apache2

    /opt/bitnami/apache2/conf/httpd.conf:542:Include "/opt/bitnami/apps/django/conf/django.conf"
    /opt/bitnami/apache2/conf/bitnami/bitnami-apps-prefix.conf:2:Include "/opt/bitnami/apps/django/django_projects/Project/conf/httpd-prefix.conf"

Search for Virutal on /opt/bitnami/apache2

    /opt/bitnami/apache2/conf/include/http_vhost.h:19: * @brief Virtual Host package
    /opt/bitnami/apache2/conf/include/http_vhost.h:21: * @defgroup APACHE_CORE_VHOST Virtual Host Package
    /opt/bitnami/apache2/conf/include/http_vhost.h:51: * @param s The list of Virtual Hosts.
    /opt/bitnami/apache2/conf/include/http_vhost.h:66: * Callback function for every Name Based Virtual Host.
    /opt/bitnami/apache2/conf/include/http_vhost.h:78: * @param func_cb Function called for every Name Based Virtual Host for this
    /opt/bitnami/apache2/conf/conf/original/extra/httpd-vhosts.conf:1:# Virtual Hosts
    /opt/bitnami/apache2/conf/conf/original/extra/httpd-ssl.conf:77:## SSL Virtual Host Context
    /opt/bitnami/apache2/conf/conf/original/httpd.conf:466:# Virtual hosts
    /opt/bitnami/apache2/conf/conf/extra/httpd-vhosts.conf:1:# Virtual Hosts
    /opt/bitnami/apache2/conf/conf/extra/httpd-ssl.conf:77:## SSL Virtual Host Context
    /opt/bitnami/apache2/conf/conf/httpd.conf:467:# Virtual hosts
    /opt/bitnami/apache2/conf/conf/bitnami/bitnami.conf:1:# Default Virtual Host configuration.
    /opt/bitnami/apache2/conf/conf/bitnami/bitnami.conf:33:# Default SSL Virtual Host configuration.
    /opt/bitnami/apache2/conf/conf/bitnami/bitnami-apps-vhosts.conf:1:# Bitnami applications installed in a Virtual Host


vim /opt/bitnami/apache2/conf/bitnami/bitnami-apps-prefix.conf

-- ---------------------------------------------------------------------------------------------------
1 - To install a new project on bitnami django VM:
-- ---------------------------------------------------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------
2 - create file <app>/conf/httpd-app.conf
-- ---------------------------------------------------------------------------------------------------
    <IfDefine !IS_DJANGOSTACK_LOADED>
    Define IS_DJANGOSTACK_LOADED
    WSGIDaemonProcess wsgi-djangostack processes=2 threads=15 display-name=%{GROUP}
    </IfDefine>

    <Directory "/opt/bitnami/apps/django/django_projects/Project/Project">
        Options +MultiViews
        AllowOverride All
        <IfVersion < 2.3 >
            Order allow,deny
            Allow from all
        </IfVersion>
        <IfVersion >= 2.3>
            Require all granted
        </IfVersion>

        WSGIProcessGroup wsgi-djangostack

    WSGIApplicationGroup %{GLOBAL}
        <IfVersion < 2.3 >
            Order allow,deny
            Allow from all
        </IfVersion>
        <IfVersion >= 2.3>
            Require all granted
        </IfVersion>

    </Directory>

    Alias /static "/opt/bitnami/apps/django/lib/python2.7/site-packages/django/contrib/admin/static"
    WSGIScriptAlias /Project '/opt/bitnami/apps/django/django_projects/Project/Project/wsgi.py'



-- ---------------------------------------------------------------------------------------------------
3  - create file <app>/conf/httpd-prefix.conf
-- ---------------------------------------------------------------------------------------------------
    # Include file
    Include "/opt/bitnami/apps/django/django_projects/Project/conf/httpd-app.conf"



-- ---------------------------------------------------------------------------------------------------
4 -create file <app>/conf/httpd-vhosts.conf
-- ---------------------------------------------------------------------------------------------------
    <VirtualHost *:80>
        ServerName djangostack.example.com
        ServerAlias www.djangostack.example.com
        DocumentRoot "/opt/bitnami/apps/django/django_projects/Project/Project"

        Include "/opt/bitnami/apps/django/django_projects/Project/conf/httpd-app.conf"
    </VirtualHost>

    <VirtualHost *:443>
        ServerName djangostack.example.com
        ServerAlias www.djangostack.example.com
        DocumentRoot "/opt/bitnami/apps/django/django_projects/Project/Project"
        SSLEngine on
        SSLCertificateFile "/opt/bitnami/apps/django/django_projects/Project/conf/certs/server.crt"
        SSLCertificateKeyFile "/opt/bitnami/apps/django/django_projects/Project/conf/certs/server.key"

        Include "/opt/bitnami/apps/django/django_projects/Project/conf/httpd-app.conf"
    </VirtualHost>

-- ---------------------------------------------------------------------------------------------------
5 - Apache
-- ---------------------------------------------------------------------------------------------------
    Edit file and change Project to the <app_name>:
        vim /opt/bitnami/apache2/conf/bitnami/bitnami-apps-prefix.conf
            Include "/opt/bitnami/apps/django/django_projects/<app_name>/conf/httpd-prefix.conf"

restart apache
sudo /opt/bitnami/ctlscript.sh restart apache
