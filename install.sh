sudo su - root
apt-get -y update 

apt-get -y install python-setuptools git git-core redis-server libhiredis-dev curl 

easy_install pip

pip install virtualenv 

curl https://raw.github.com/creationix/nvm/master/install.sh | sh

source ~/.nvm/nvm.sh

nvm install v0.10.7

git clone git@github.com:abishekk92/spell_check.git && cd spell_check
 
cp -f back_up/dump.rdb /var/lib/redis/

virtualenv --distribute venv

source venv/bin/activate 


git clone git@github.com:seomoz/pyreBloom.git && cd pyreBloom && python setup.py install

cd ..

pip install -r requirements.txt

python load_data.py

python spell.py &

cd spell_client 

nvm use v0.10.7

npm install && npm start 
