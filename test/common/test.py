import sys
import os

print(os.path.abspath('.'))
print(os.path.abspath('__file__'))
print(os.path.abspath(os.path.dirname('.')))
print(os.path.abspath(os.path.dirname('__file__')))


print(os.path.dirname(os.path.abspath(".")))
print(sys.path(1).append(os.path.dirname(os.path.abspath('.'))))