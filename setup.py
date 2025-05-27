from setuptools import setup, find_packages

python-dotenv
google-auth-oauthlib

google-api-python-client
PyYAML

setup(
    name='ytcli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'google-auth-oauthlib',
        'google-api-python-client',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'ytcli = ytcli.cli:main',
        ],
    },
    author='lgtkgtv@gmail.com',
    description='CLI for managing YouTube playlists',
    license='MIT',
)

