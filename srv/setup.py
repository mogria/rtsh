from setuptools import setup, find_packages

setup(
    name = 'rtsh.srv',
    version = '0.1',
    description = 'Python Server for the Real Time Strategy Shell Game',
    author = 'wtjerry, mogria',
    author_email = 'wtjerry123@gmail.com, m0gr14@gmail.com',
    keywords = 'real-time strategy game server',
    url = 'https://github.com/mogria/rtsh',

    packages = find_packages(),
    scripts = ['srv.py'],
    license = 'GPLv2+',
    install_requires = [
        'numpy',
        'fake-factory'
    ]
)

