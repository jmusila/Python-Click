from setuptools import setup 

setup(
    name = 'clisample',
    version = '1.0',
    install_requires = ['Click',],
    py_modules = ['clisimple',],
    entry_points = '''
    [consolescripts]
    hello=clisimple:hello
    '''
)