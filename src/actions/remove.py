import shutil
import os.path
from utils.package import Package


def handle(package_name):
    path = os.path.join('python_modules', package_name)
    package_file = Package('.')

    if package_file.has_dependency(package_name):
        package_file.remove_dependency(package_name)
        package_file.save()

    if os.path.isdir(path):
        shutil.rmtree(path)

    print('Package {} has been removed'.format(package_name))


