import inspect

if not hasattr(inspect, 'getargspec'): # 修复
    inspect.getargspec = inspect.getfullargspec
    
from taolib.doc import sites

namespace = sites('docs', target='docs/_build/html')
