source /root/.profile
cd /vagrant/spell_client

nvm use v0.10.7

nohup npm start > /var/log/spell/spell_client/express.log  2>&1 &
