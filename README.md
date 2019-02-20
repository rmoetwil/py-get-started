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
- [Miniconda](https://conda.io/en/latest/miniconda.html)
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

### Freeze and Restore dependencies
Once you have installed some dependencies you might want to share your project.
To create a list of dependencies run:
```
pip freeze --local > requirements.txt
```

To install a fresh environment with the dependencies listed run:
```
pip install -r requirements.txt
```

### Where to find Python packages
Python packages can be found [here](https://pypi.org/).


# Jupyter
To be able to run Jupyter notebooks install Jupyter:
```
python3 -m pip install jupyter
```

Execute the following to run a jupyter notebook called `notebook`.
```
jupyter notebook
```
