# Define a class for managing SSH client configuration
class { 'ssh::client': }

# Configure IdentityFile
file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
  ensure => present,
}

# Disable PasswordAuthentication
file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
  ensure => present,
}
