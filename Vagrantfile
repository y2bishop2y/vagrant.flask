# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "precise64"

  config.vm.box_url = "http://files/vagrantup.com/precise64.box"

  config.vm.boot_mode = :gui


  config.vm.forward_port 5000, 5000
  

  # Enable provisiong with Puppet stand alone. Puppet manifests
  # are contained in a directory path relative to this Vagrantfile
  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "puppet/manifests"
    puppet.module_path    = "puppet/modules"
    puppet.manifest_file  = "base.pp"
   end

  # Application provision
  config.vm.provision :shell, :inline => "cd /vagrant && stdbuf -o0 fab build; exit 0"

end
