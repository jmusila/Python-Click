from setuptools import setup, find_packages

setup(
    name='clisample',
    version='1.0',
    install_requires=['Click', ],
    py_modules=['find_packages', ],
    entry_points='''
    [consolescripts]
    hello=clisimple:hello
    '''
)
