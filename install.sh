apt-get -y update 

apt-get -y install python-dev python-setuptools git git-core redis-server libhiredis-dev curl gcc 

easy_install pip

pip install virtualenv 

curl https://raw.github.com/creationix/nvm/master/install.sh | sh

source ~/.nvm/nvm.sh

nvm install v0.10.7

/etc/init.d/redis-server stop

cd /vagrant

cp -f conf/redis.conf /etc/redis/

/etc/init.d/redis-server start

cd venv || virtualenv --distribute venv;

cd /vagrant
source venv/bin/activate 

pip install -r requirements.txt

cd pyreBloom && python setup.py install

cd /vagrant

python spell.py &

cd spell_client 

nvm use v0.10.7

npm install || mkdir -p /var/log/spell && mkdir -p /var/log/spell/spell_client
