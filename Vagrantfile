# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

    config.vm.box = "precise64"
    #Start of from 
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"

    #SSH Settings
    config.ssh.private_key_path = "~/.ssh/id_rsa"
    config.ssh.forward_agent = true
    # Create a forwarded port mapping which allows access to a specific port
    # within the machine from a port on the host machine. In the example below,
    # accessing "localhost:8080" will access port 80 on the guest machine.
    config.vm.network :forwarded_port, guest: 80, host: 8080
    config.vm.network :forwarded_port, guest: 3000, host: 3000
    #Install and start all the process
    #TODO: Break these into individual tasks for better readibility, abstraction is bad here? 
    config.vm.provision :shell, :path => "install.sh"
end
