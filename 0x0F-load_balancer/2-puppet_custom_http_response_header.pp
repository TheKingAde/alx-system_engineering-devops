# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define a custom fact to get the hostname of the server
# This fact will be used to dynamically set the value of the X-Served-By header
# Save this file as /etc/puppetlabs/facter/facts.d/hostname_fact.sh
file { '/etc/puppetlabs/facter/facts.d/hostname_fact.sh':
  ensure  => file,
  content => '#!/bin/bash\necho "hostname=$(hostname)"',
  mode    => '0755',
}

# Configure Nginx with a custom header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('your_module/nginx_config.erb'),
  notify  => Service['nginx'],
}

# Symbolic link to enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
