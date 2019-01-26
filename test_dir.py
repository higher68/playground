import os

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
dir_path = os.path.join(dirname, '../hoya')

print(abspath)
print(dirname)
print(dir_path)
