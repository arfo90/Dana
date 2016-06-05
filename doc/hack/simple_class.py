class SimpleClass:
    attr = 100
    __privateValue = 500 ##'__' make it private
    def __init__(self):
        print 'constructor'
    
    def parentMetod(self, attr):
        print SimpleClass.attr
        
class ChildSimple(SimpleClass):
    def __init__(self):
        print 'testing'
        
## a = ChildSimple()        