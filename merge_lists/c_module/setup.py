from distutils.core import setup, Extension
setup(name = 'merge', version = '1.0',  \
    ext_modules = [Extension('merge', ['merge.c'])])
