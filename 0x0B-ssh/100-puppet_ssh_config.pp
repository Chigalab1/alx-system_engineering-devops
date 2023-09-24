#!/usr/bin/env bash
# Change the SSH Client confuration file
file { 'etc/ssh/ssh_config':
	ensure => present,
content =>"

	# ssh host client config
	host*
  	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
