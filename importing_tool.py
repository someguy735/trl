from tools_script import search_duckduckgo,search_duckduckgo_without_docs
from inspect import getsource,getclosurevars

#print(getsource(search_duckduckgo))
#print(search_duckduckgo.__doc__)
#print(getsource(search_duckduckgo_without_docs))
#print(search_duckduckgo_without_docs.__doc__)

print(getclosurevars(search_duckduckgo))

