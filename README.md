spell_check
===========

Real time spell checking on twitter stream using naive clustering, Dmetaphones and Bloomfilter goodness.

__NOTE__:

Before you run the app. Make sure you enter your auth_keys and secrets in conf/app.config, a sample config is provided.

```ini
[twitter]
twitter_cons_key: consumer-key 
twitter_cons_secret: consumer-secret
twitter_auth_token: auth_token
twitter_auth_secret: auth_secret
```

A Vagrant box is distributed if you want to set up the box locally and play with it. You will need to have Vagrant and Virtual Box installed. If not however follow the instructions [here](http://docs-v1.vagrantup.com/v1/docs/getting-started/).


__Usage__ :

- Start the vagrant by issuing 

```bash
    vagrant up
```
- The vagrant forwards the network port 3000 of the vagrant to localhost's 3000, so you can go to your favorite browser and visit the [app](http://localhost:9000)

- Should you need to ssh into the machine and get your hands dirty. 

```bash
    vagrant ssh
```

__Deploying to AWS__:

If setting this up locally is an overkill, you might as well deploy this on AWS or any other provider supported by vagrant using

```bash

vagrant up --provider <provider-name>
```

However, the support for different providers by Vagrant is through plugins. 

Please follow the succint instruction [here](https://github.com/mitchellh/vagrant-aws) for deploying to AWS
