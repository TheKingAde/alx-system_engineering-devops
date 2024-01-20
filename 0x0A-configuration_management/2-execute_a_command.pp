# This Puppet manifest kills a process named 'killmenow' using the 'exec' resource and 'pkill'.
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
}
