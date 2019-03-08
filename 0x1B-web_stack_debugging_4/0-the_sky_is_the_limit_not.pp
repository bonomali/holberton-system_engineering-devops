# Edits a an Nginx configuration file to up the request limit
exec { 'increase limit':
  command  => 'sed -i \'s/15/2000/\' /etc/default/nginx && sudo service nginx restart',
  provider => 'shell'
}
