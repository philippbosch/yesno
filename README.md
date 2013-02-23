yesno
=====

A collection of classes that make it easy to answer a yes/no question 
automatically and feed one of these `is__________.com` websites.


Examples
--------

### Web Content

**Question**: Does the web page at http://edition.cnn.com/ contain the keyword «obama»?  
**Answer**: Yes. Four times.

```python
from yesno.web import DoesWebPageContainKeywordQuestion
q = DoesWebPageContainKeywordQuestion(url='http://edition.cnn.com/', keyword='obama')
answer, extra = q.answer()
```

### Weather

**Question**: Is it at least 13°C in Berlin, Germany?  
**Answer**: No. It's -2°C.

```python
from yesno.weather import CurrentTemperatureQuestion
q = CurrentTemperatureQuestion(location='Berlin, Germany', min=13, unit=CurrentTemperatureQuestion.CELSIUS)
answer, extra = q.answer()
```


Web App
-------

If you want to, you can use yesno's built-in webserver to serve your one-page website.

```python
from yesno import App
from yesno.weather import CurrentTemperatureQuestion

question = CurrentTemperatureQuestion(location='Berlin, Germany', min=13, unit=CurrentTemperatureQuestion.CELSIUS)
app = App(question)
app.run()
```
