# update soft limit and hard limit for the user holberton
exec { 'update soft limit':
  command  => "sed -i 's/^holberton soft nofile.*/holberton soft nofile 2000/' /etc/security/limits.conf",
  provider => 'shell',
}

exec { 'update hard limit':
  command  => "sed -i 's/^holberton hard nofile.*/holberton hard nofile 2000/' /etc/security/limits.conf",
  provider => 'shell',
}