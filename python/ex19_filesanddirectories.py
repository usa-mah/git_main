from pathlib import Path


# Absolute path


# Relative path
path = Path("ecommerce_pkg")

print(path.exists())

path2 = Path("emails")
path2.mkdir() # make the "emails" directroy
path2.rmdir() # remove the "emails" directroy


# iterate over all the files in a direcrory
path3 = Path()

for file in path3.glob('*.py'): # search for all the files with .py extension
    print(file)

