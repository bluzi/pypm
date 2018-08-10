# pypm
**Py**thon **P**ackage **M**anager is a package manager for Python based on npm

## Why?
Because npm is the best package solution ever invented, and the current solutions for Python packages suck.

## How?
### Installation
pypm is still under development and we don't have an official release yet.
If you want to try it, you can clone this repository and use it from the source.

### Creating a package
Create a directory and navigate into it, then type `pypm init` and follow the interactive wizard.
pypm will create a `package.json` file with the information you supplied.
You can modify `package.json` and adapt it to your needs, it works just like npm's package file.

### Installing a package
Type `pypm install [package-name]`.
By default, pypm will install packages locally and will try to add a dependency record to the cloest `package.json`, if you want to install a pakcage globally add the `-g` flag.

### Removing a package
`pypm remove [package-name]` will remove a package. If you want to remove a global package, add the `-g` flag.

## Supprt and contributions
Feel free to create feature requests as issues. If you want to contribute code, please open an issue first describing what you want to do.

## License
pypm is completely open source and the source code is licensed under the MIT license.