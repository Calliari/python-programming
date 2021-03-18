#### Install development tools for python 

```
# centos
sudo yum groupinstall -y "development tools"
sudo yum install -y wget vim lsof which words libffi-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel postgresql-devel

cd /usr/src
sudo sh -c 'wget http://python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz && tar xf Python-3.7.2.tar.xz'
sudo sh -c 'Python-3.7.2/configure --enable-optimizations && make altinstall'

# if fails add the path omn the visudo file (i.g "Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin")
sudo pip3.7 install --upgrade pip
```

```
# ubuntu
sudo apt groupinstall -y "development tools"
sudo apt install -y wget vim lsof which words libffi-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel postgresql-devel

cd /usr/src
sudo sh -c 'wget http://python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz && tar xf Python-3.7.2.tar.xz'
sudo sh -c 'Python-3.7.2/configure --enable-optimizations && make altinstall'

# if fails add the path omn the visudo file (i.g "Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin")
sudo pip3.7 install --upgrade pip
```
