"""Exploring modules with dir()"""

import sys

# print(dir(sys))

print(
    f"Python Version: {sys.version}\n"
)  # Prints the Python Version you are currently using.
print(
    f"Platform: {sys.platform}\n"
)  # Prints the platform you are using right now. In this case Microslop Windows.
print(f"Python's Copyright: {sys.copyright}\n")  # Prints Python's Copyright Licenses
print(
    f"Python's Path: {sys.path}\n"
)  # Prints a list of directories where the interpreter finds the modules to import.
print(
    f"Modules: {sys.modules}\n"
)  # sys.modules is a dictionary that maps module name to modules which have already been loaded.
