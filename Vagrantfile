# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"

  config.vm.box_check_update = false

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  config.vm.provision "telemetry", type: :ansible, playbook: "provision/playbook.yml"

  config.vm.define "database" do |db|
    db.vm.network "private_network", ip: "192.168.56.20"
    db.vm.network "forwarded_port", guest: 9100, host:9110
    
    db.vm.provision :ansible, playbook: "provision/database/playbook.yml"
  end
  config.vm.define "webserver" do |ws|
    ws.vm.network "private_network", ip: "192.168.56.30"
    ws.vm.network "public_network", ip: "192.168.0.102"
    ws.vm.network "forwarded_port", guest: 9100, host: 9111


    ws.vm.provision "install", type: :ansible, playbook: "provision/webserver/playbook.yml"
  end

end
