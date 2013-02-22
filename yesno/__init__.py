class Question(object):
    YES = True
    NO = False
    
    def __init__(self, **kwargs):
        self.params = kwargs

    def answer(self):
        raise NotImplementedError
