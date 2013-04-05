# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "precise64"

  config.vm.box_url = "http://files/vagrantup.com/precise64.box"

  # config.vm.boot_mode = :gui

  #--------------------------
  # Config the app server 
  #--------------------------
  config.vm.define "app" do |app| 
    # Figure out what this options is on V2 
    # app.vm.boot_mode  :gui
    app.vm.network  :private_network, ip: "33.33.33.10"
    app.vm.hostname = "appserver01.local"
    app.vm.network :forwarded_port, host: 5000, guest: 5000, auto_correct: true

    # Enable provisiong with Puppet stand alone. Puppet manifests
    # are contained in a directory path relative to this Vagrantfile
    app.vm.provision :puppet do |puppet|
      puppet.manifests_path = "puppet/manifests"
      puppet.module_path    = "puppet/modules"
      puppet.manifest_file  = "app.pp"
    end

    app.vm.provision :shell, :inline => "cd /vagrant && stdbuf -o0 fab build; exit 0"
  end

  #--------------------------
  #--------------------------
  config.vm.define "db" do |db|
    # Have to figure out what boot_mode is on version 2
    # db.vm.boot_mode = :gui
    db.vm.network :private_network, ip: "33.33.33.11"
    db.vm.hostname = "dbserver01.local"
    db.vm.provision :puppet do |puppet|
      puppet.manifests_path = "puppet/manifests"
      puppet.module_path    = "puppet/modules"
      puppet.manifest_file  = "dbserver.pp"
    end
  end


  # Application provision
  # config.vm.provision :shell, :inline => "cd /vagrant && stdbuf -o0 fab build; exit 0"


end
