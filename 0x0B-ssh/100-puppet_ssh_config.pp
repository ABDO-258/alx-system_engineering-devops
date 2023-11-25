#  changes to our configuration file
file_line {'turn password off':
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}

file_line {'define identity file':
    path  => '/etc/ssh/ssh_config',
    line  => 'IdentityFile ~/.ssh/school',
}