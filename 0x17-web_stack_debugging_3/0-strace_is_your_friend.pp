# debug the problem of why apache2 return 500

exec { "let's fix":
    provider => 'shell',
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
