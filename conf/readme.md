##Configure the VM (OSX)

Edit file:

    vim /Applications/bitnami-djangostack-1.7-1/apache2/conf/bitnami/bitnami-apps-prefix.conf

and change the application diretory to poin to:

    /Applications/bitnami-djangostack-1.7-1/apps/django/django_projects/rural_sustentavel/conf/server/httpd-prefix.conf

Restart Apache:

    /Applications/bitnami-djangostack-1.7-1/ctlscript.sh (start|stop|restart) apache

##Configure the VM (Linux)

Edit file:

    vim #TBD/apache2/conf/bitnami/bitnami-apps-prefix.conf

and change the application diretory to poin to:

    #TBD/apps/django/django_projects/rural_sustentavel/conf/server/httpd-prefix.conf

Restart Apache:

    #TBD/ctlscript.sh start apache
    #TBD/ctlscript.sh stop apache
    #TBD/ctlscript.sh restart apache


##Configure the SERVER

Edit file:

    sudo vim /opt/bitnami/apache2/conf/bitnami/bitnami-apps-prefix.conf

and change the application diretory to poin to:

    /opt/bitnami/apps/django/django_projects/rural_sustentavel/conf/server/httpd-prefix.conf

Restart Apache:

    sudo /opt/bitnami/ctlscript.sh restart apache
