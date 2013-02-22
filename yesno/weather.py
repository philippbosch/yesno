# -*- coding: utf-8 -*-

import yweather
from . import Question


class CurrentTemperatureQuestion(Question):
    CONSTRAINT_MIN = 1
    CONSTRAINT_MAX = 2
    CONSTRAINT_EXACT = 3

    FAHRENHEIT = "F"
    CELSIUS = "C"

    def __init__(self, **kwargs):
        self.client = yweather.Client()

        # Determine location
        if 'location' in kwargs:
            self.location = kwargs['location']
            self.woeid = self.client.fetch_woeid(kwargs['location'])
        elif 'woeid' in kwargs:
            self.location = None
            self.woeid = str(kwargs['woeid'])
        else:
            raise Exception("No `location` or `woeid` argument provided.")

        # Determine contraint
        if 'min' in kwargs:
            self.constraint = (self.CONSTRAINT_MIN, int(kwargs['min']))
        elif 'max' in kwargs:
            self.constraint = (self.CONSTRAINT_MAX, int(kwargs['max']))
        elif 'exact' in kwargs:
            self.constraint = (self.CONSTRAINT_EXACT, int(kwargs['exact']))
        else:
            raise Exception("No constraint provided. Please use `min`, `max` or `exact` keyword")

        # Determine temperature unit
        self.unit = self.FAHRENHEIT
        if 'unit' in kwargs:
            if kwargs['unit'] == self.CELSIUS:
                self.unit = self.CELSIUS

    def answer(self):
        weather = self.client.fetch_weather(self.woeid, metric=self.unit==self.CELSIUS)
        temp = int(weather['condition']['temp'])

        type_, value = self.constraint
        extra = u"It's {0}°{1}.".format(temp, self.unit)

        if type_ == self.CONSTRAINT_MIN:
            answer = temp >= value and self.YES or self.NO
        elif type_ == self.CONSTRAINT_MAX:
            answer = temp <= value and self.YES or self.NO
        elif type_ == self.CONSTRAINT_EXACT:
            answer = temp == value and self.YES or self.NO

        return (answer, extra)

    def __unicode__(self):
        if self.constraint[0] == self.CONSTRAINT_MIN:
            comparison = "at least"
        elif self.constraint[0] == self.CONSTRAINT_MAX:
            comparison = "at most"
        elif self.constraint[0] == self.CONSTRAINT_EXACT:
            comparison = "exactly"

        return u"Is the current temperature at {location} {comparison} {temperature}°{unit}?".format(
            location=self.location or "WOEID {0}".format(self.woeid),
            comparison=comparison,
            temperature=self.constraint[1],
            unit=self.unit
        )
