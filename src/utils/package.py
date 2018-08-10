import json

def parse(path = '.'):
    with open(path) as packageFile:
        return json.load(packageFile)

def save(path, package):
    with open(path, 'w') as packageFile:
        json.dump(package, packageFile)