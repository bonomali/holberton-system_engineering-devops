# Edits a Wordpress config file to use the correct file extension
exec { 'fix wp':
  command  => 'sed -i \'s/phpp/php/\' /var/www/html/wp-settings.php',
  provider => 'shell'
}
