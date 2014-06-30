from distutils.core import setup

setup (
  name = 'Wcat',
  version = '0.1',
  author = 'Thomas Lant',
  author_email = 'thomas.lant@gmail.com',
  packages = ['wcat'],
  scripts = ['bin/wcat'],
  license = 'wcat/LICENSE.txt',
  description = 'A simple tool to output text from web pages behind a CAS or basic HTTP auth login',
  long_description = open('wcat/README.md').read(),
)
