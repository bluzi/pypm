import json
import os.path
import subprocess


def get_closest_package_file(path):
    file_path = os.path.join(path, 'package.json')
    if os.path.isfile(file_path):
        return file_path
    elif os.path.isdir(os.path.join(path, '..')):
        return get_closest_package_file(os.path.join(path, '..'))
    else:
        return None


class Package: 
    def __init__(self, path=None, explicit_path=False):
        if path:
            if explicit_path:
                file_path = os.path.join(path, 'package.json')
            else:
                file_path = get_closest_package_file(path)

            if not os.path.isfile(file_path):
                if explicit_path:
                    raise ValueError('Unable to find package.json in {}'.format(path))
                else:
                    raise ValueError('Unable to find package.json in {} or any of its parent directories'.format(path))


            with open(file_path) as packageFile:
                contents = json.load(packageFile)
                self.contents = contents
                self.path = file_path
        else:
            self.contents = {}

    def add_dependency(self, package_name):
        if not self.contents.dependencies:
            self.contents.dependencies = list()

        self.contents.dependencies.append(package_name)

    def has_dependency(self, package_name):
        if not self.contents.dependencies:
            return False

        return package_name in self.contents.dependencies

    def remove_dependency(self, package_name):
        if self.contents.dependencies:
            self.contents.dependencies.remove(package_name)

    def run(self, script_name):
        if script_name in self.contents.scripts:
            script = self.contents.scripts[script_name].split()
            subprocess.Popen(script)

    def save(self, path=None):
        if not path:
            path = self.path

            with open(os.path.join(path, 'package.json'), 'w') as package_file:
                json.dump(self.contents, package_file)