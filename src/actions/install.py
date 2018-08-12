import os.path
from utils.package import Package
from utils import client


def handle(package):
    if package:
        install_package(package)
    else:
        install_dependencies()


def install_package(package_name):
    print('installing {}'.format(package_name))
    downloaded_package_file = client.download(package_name, './python_modules/')

    package_file = Package('.')
    package_file.add_dependency(package_name, downloaded_package_file.get_version())
    package_file.save()


def install_dependencies():
    package_file = Package('.')
    for dependency_name in package_file.get_dependencies():
        if _dependency_exists(dependency_name):
            print('Dependency {} already exists'.format(dependency_name))
        else:
            client.download(dependency_name, './python_modules/')
            print('Installed {}'.format(dependency_name))


def _dependency_exists(dependency_name):
    return os.path.isdir(os.path.join('python_modules', dependency_name))