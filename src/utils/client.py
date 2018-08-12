import requests
import os.path
import urllib.parse
from utils.package import Package
from utils import config
import pathlib


def download(package_name, dest, index=None):
    if not index:
        index = config.index

    response = requests.get(urllib.parse.urljoin(index, package_name))
    data = response.json()

    if 'error' in data:
        if data['error'] == 'not_found':
            raise ValueError('Unable to find package "{}"'.format(package_name))

    package_dir = os.path.join(dest, package_name)

    for file in data['files']:
        path = os.path.join(package_dir, file['path'])
        pathlib.Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
        with open(path, 'w+') as local_file:
            local_file.write(file['contents'])

    package_file = Package(package_dir, explicit_path=True)
    package_file.run('postinstall')

    return package_file


def publish(package_name, version, files, index=None):
    if not index:
        index = config.index

    response = requests.post(urllib.parse.urljoin(index, package_name))
    response.json()