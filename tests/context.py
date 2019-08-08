import sys
from os.path import abspath, join, dirname, pardir
root_path = abspath(join(dirname(__file__), pardir))
if root_path not in sys.path:
    sys.path.insert(0, root_path)
test_path = join(root_path, "tests")
if test_path not in sys.path:
    sys.path.insert(0, test_path)
import tfs