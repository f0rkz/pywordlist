from setuptools import setup, find_packages

requires = ['requests==2.18.1']

setup(name='pywordlist',
      version='0.0.2',
      description='Random phrase generator. https://xkcd.com/936/',
      url='http://github.com/f0rkz/pywordlist',
      author='f0rkz',
      author_email='f0rkz@f0rkznet.net',
      license='MIT',
      packages=['pywordlist'],
      install_requires=[requires],
      zip_safe=True)
