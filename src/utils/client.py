import requests
import os.path
import urllib.parse
from utils.package import Package
from utils import config


def download(package_name, dest, index=None):
    if not index:
        index = config.index

    response = requests.get(urllib.parse.urljoin(index, package_name))
    response.json()

    if response.error == 'not_found':
        raise ValueError('Unable to find package "{}"'.format(package_name))

    for file in response.files:
        path = os.path.join(dest, file.path)
        with open(path, 'w') as local_file:
            local_file.write(file.contents)

    package_file = Package(dest, explicit_path=True)
    package_file.run('postinstall')

def publish(package_name, version, files, index=None):
    if not index:
        index = config.index

    response = requests.post(urllib.parse.urljoin(index, package_name))
    response.json()