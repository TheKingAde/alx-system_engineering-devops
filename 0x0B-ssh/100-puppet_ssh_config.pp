class { 'ssh::client': }

file_line { 'Declare identity file':
  ensure => present,  # Moved ensure to the beginning
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}

file_line { 'Turn off passwd auth':
  ensure => present,  # Moved ensure to the beginning
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
