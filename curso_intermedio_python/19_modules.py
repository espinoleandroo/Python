import sys
print(sys.path)

import re
text = 'Mi numero de Telefono es 123 456 789'
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,2,1,1,2,32,1,1,1]
counter = collections.Counter(numbers)
print(counter)