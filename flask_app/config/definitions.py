import os

# VARIANT 1:
# root directory for build file
# ROOT_DIR = os.path.realpath(os.path.join(os.getcwd(), '..'))

# VARIANT 2:
# root directory for "run"
# ROOT_DIR = os.path.realpath(os.path.join(os.getcwd(), '../../..'))
# ROOT_DIR = os.path.realpath(os.path.join(os.getcwd(), '..'))



# VARIANT 3:
# root directory for server deployment
ROOT_DIR = os.path.realpath(os.path.join(os.getcwd(), '../app'))
