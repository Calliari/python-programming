# This is a study guide for the PCEP certification
https://pythoninstitute.org/pcep



Installation of the python3 version
Reference page: https://github.com/pyenv/pyenv

Instructions:
```
# Clone the repo
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Set up your shell environment for Pyenv (it can be done with '~/.bash_profile', '~/.bashrc' or any other bash alternative like Zsh)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

# Restart your shell
exec "$SHELL"

# install the version required, in this case 'python 3.9'
pyenv install 3.9.6

# Check the version installed
pyenv versions

# Confirm the version to be set
pyenv shell 3.9.6

# Check the version
python -V


# Install pip
pip3 install --upgrade pip

```



