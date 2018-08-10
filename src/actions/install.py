from utils import package

def handle(package):
    if (package): 
        install_package(package)
    else: 
        install_dependencies()

def install_package(package):
    print('installing {}'.format(package))

def install_dependencies():
    packageFile = package.parse()