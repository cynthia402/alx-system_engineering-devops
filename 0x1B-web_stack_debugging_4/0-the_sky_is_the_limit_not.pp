# bring that limit higher found in /etc/default/nginx to more than 15

exec { '/usr/bin/env sed -i s/15/1500/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
