# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"

  config.vm.box_check_update = false

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  config.vm.define "database" do |vma|
    vma.vm.network "private_network", ip: "192.168.56.20"
    
    vma.vm.provision :ansible, playbook: "provision/database/playbook.yml"
  end
  config.vm.define "webserver" do |vmb|
    vmb.vm.network "private_network", ip: "192.168.56.30"
    vmb.vm.network "public_network", ip: "192.168.0.102"


    vmb.vm.provision "install", type: :ansible, playbook: "provision/webserver/playbook.yml"
  end

end
