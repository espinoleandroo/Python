from pkg.mod_1 import fun_1, fun_2
from pkg.mod_2 import fun_3, fun_4

print(fun_1())
print(fun_2())
print(fun_3())
print(fun_4())

import pkg
print(pkg.URL)
print(pkg.mod_1.fun_1())

