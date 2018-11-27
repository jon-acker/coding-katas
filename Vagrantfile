# -*- mode: ruby -*-
# vi: set ft=ruby :
# Automatically download required plugins
required_plugins = %w( vagrant-hostsupdater nugrant )

return if !Vagrant.plugins_enabled?

plugins_to_install = required_plugins.select { |plugin| !Vagrant.has_plugin? plugin }

if plugins_to_install.any?
  system "vagrant plugin install #{plugins_to_install.join(' ')}"
  exit system 'vagrant up'
end

config.vm.provision 'ansible-local' do |ansible|

end
