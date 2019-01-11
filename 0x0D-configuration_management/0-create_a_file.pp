# Creates a file in /tmp with certain requirements
file { '/tmp/holberton':
  owner   => www-data,
  group   => www-data,
  content => 'I love Puppet',
  mode    => '0744'
}
