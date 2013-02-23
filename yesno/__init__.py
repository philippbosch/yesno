from flask import Flask, render_template


class Question(object):
    YES = True
    NO = False

    def __init__(self, **kwargs):
        self.params = kwargs

    def answer(self):
        raise NotImplementedError


class App(Flask):
    def __init__(self, *args, **kwargs):
        args = list(args)
        self.question = args.pop(0)
        super(App, self).__init__('__main__', *tuple(args), **kwargs)
        self.add_url_rule('/', 'index', self.index)

    def index(self):
        answer, extra = self.question.answer()
        return render_template('index.html', question=unicode(self.question), answer=answer, extra=extra)


class InvalidArgumentError(Exception):
    pass


class EmptyArgumentError(Exception):
    pass

