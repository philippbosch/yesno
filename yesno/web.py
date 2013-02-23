# -*- coding: utf-8 -*-

import re
try:
    import requests
except ImportError:
    raise Exception('`requests` library not found. Please install with e.g. `pip install requests`.')
from . import Question, EmptyArgumentError


class DoesWebPageContainKeywordQuestion(Question):
    def __init__(self, url, keyword):
        if not len(url) or not len(keyword):
            raise EmptyArgumentError
        self.url = url
        self.keyword = keyword

    def get_num_occurrences(self, content):
        return content.lower().count(self.keyword.lower())

    def answer(self):
        req = requests.get(self.url)
        occurrences = self.get_num_occurrences(req.content)
        answer = bool(occurrences) and self.YES or self.NO

        if occurrences == 1:
            extra = 'It does.'
        elif occurrences == 2:
            extra = 'Twice, to be precise.'
        elif occurrences > 2 and occurrences < 13:
            numbers = ['three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
            extra = '{0} times.'.format(numbers[occurrences-3].capitalize())
        elif occurrences >= 13:
            extra = '{0} times even.'.format(occurrences)
        else:
            extra = ''

        return (answer, extra)

    def __unicode__(self):
        return u'Does the web page at {url} contain the keyword «{keyword}»?'.format(
            url=self.url,
            keyword=self.keyword,
        )


class DoesWebPageMatchRegexQuestion(DoesWebPageContainKeywordQuestion):
    def __init__(self, url, regex):
        if not len(url) or not len(regex):
            raise EmptyArgumentError
        self.url = url
        self.regex = regex

    def get_num_occurrences(self, content):
        return len(re.findall(self.regex, content, flags=re.I))

    def __unicode__(self):
        return u'Does the web page at {url} match the regular expression «{regex}»?'.format(
            url=self.url,
            regex=self.regex,
        )
