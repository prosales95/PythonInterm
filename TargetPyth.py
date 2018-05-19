# 1. Future imports allow to use following modules in a previous version
from __future__ import with_statement

print
# Output:

from __future__ import print_function

print(print)
# Output: <built-in function printmod>
import foo
# or
from foo import bar
import foo as foo

try:
    import urllib.request as urllib_request  # for Python 3
except ImportError:
    import urllib2 as urllib_request  # for Python 2
from future.builtins.disabled import *
from future.builtins.disabled import *

apply()
# Output: NameError: obsolete Python 2 builtin apply is disabled
