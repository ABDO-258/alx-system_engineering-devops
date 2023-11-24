# create a file in /tmp
file {'/tmp/school':
    ensure => 'file',
    mode => '0744', #sets the file permissions to 0744.
    owner => 'www-data', # sets the owner of the file to 'www-data'.
    group => 'www-data', # sets the group ownership of the file to 'www-data'.
    content => 'I love Puppet', # the content of the file
}
