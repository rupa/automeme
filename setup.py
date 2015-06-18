from setuptools import setup

setup(
    name='automeme',
    version='0.1',
    description='MAKE YOU A MEME',
    url='http://github.com/rupa/automeme',
    author='Liam Cooke, rupa',
    author_email='rupa@lrrr.us',
    license='GPL',
    packages=['automeme'],
    entry_points={
        'console_scripts': ['automeme=automeme:generate'],
    },
    zip_safe=False
)
