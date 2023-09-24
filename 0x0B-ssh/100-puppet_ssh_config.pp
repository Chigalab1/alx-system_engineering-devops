#!/usr/bin/env bash
# Change the SSH Client config file
file { 'etc/ssh/ssh_config':
	ensure => present,
content =>"

	# ssh host client configuration
	host*
  	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
