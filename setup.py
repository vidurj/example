from setuptools import setup

setup(
    name='my-awesome-helloworld-script',    # This is the name of your PyPI-package.
    version='0.1',                          # Update the version number for new releases
    install_requires=['gensim==3.0.0'],     # Requirements
    scripts=['helloworld']                  # The name of your scipt, and also the command you'll be using for calling it
    )