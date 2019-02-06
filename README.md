# Python Get Started
A Python containing several components to bootstrap your new Python adventure.

Not sure in which direction this project is going to.
It will contain some steps, links etc. to get going with Python.
Especially in the Machine Learning (ML) world.
So ML packages, Jupiter notebooks etc.

## The environment
Python 2, Python 3? Which packages? How to switch between environments? Environments bundled for Machine Learning?

To name a few:
- [Anaconda](https://www.anaconda.com/distribution/)
- can't think of the others anymore ;-)
- virtualenv

If you want to do it easy take one of the complete environments.

For me I want to get my hands dirty and want to use the most basic one and be in full control.
So it's virtualenv for me.

## virtualenv
###Install pip
Run  the following commands:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python 3 get-pip.py
```

If needed add pip to your PATH variable.

###Install virtual env

```pip install virtualenv```

To use virtualenv I suggest creating a directory that will hold all your different environments. E.g. `~/py-environments`

### Create an environment and activate it
Inside your environments directory execute 
```
python3 -m venv my-new-environment
source my-new-environment/bin/activate
```

Deactivate your environment is accomplished by just executing `deactivate` in the terminal.
