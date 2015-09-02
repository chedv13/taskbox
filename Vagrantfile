# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/vivid64"

  config.vm.network "forwarded_port", guest: 5432, host: 5433
  config.vm.network "forwarded_port", guest: 8000, host: 8001
  config.vm.network "forwarded_port", guest: 8888, host: 8889

  config.vm.synced_folder "../taskbox", "/home/vagrant/taskbox"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
  end
end
