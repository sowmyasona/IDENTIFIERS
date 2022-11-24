from ast import keyword
from keyword import kwlist


print('a'.isidentifier())
print('A'.isidentifier())
print('_'.isidentifier())
print('3_4'.isidentifier())
print('if'.isidentifier())

import keyword as kk
print(kk.kwlist)
print(len(kk.kwlist))
print(kk.iskeyword('nonlocal'))
print(kk.iskeyword('try'))
print(kk.iskeyword('while'))
print(kk.iskeyword('continue'))
print(kk.iskeyword('not'))
print(kk.iskeyword('yeild'))
print(kk.iskeyword('def'))