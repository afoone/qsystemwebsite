from django import template
import datetime

register = template.Library()

@register.filter(name="monday")
def monday(today):
   lastmonday = today - datetime.timedelta(days=today.weekday())
   return lastmonday

@register.filter(name="tuesday")
def tuesday(today):
   lastmonday = today - datetime.timedelta(days=today.weekday()-1)
   return lastmonday

@register.filter(name="wednesday")
def wednesday(today):
   lastmonday = today - datetime.timedelta(days=today.weekday()-2)
   return lastmonday

@register.filter(name="thursday")
def thursday(today):
   lastmonday = today - datetime.timedelta(days=today.weekday()-3)
   return lastmonday

@register.filter(name="friday")
def friday(today):
   lastmonday = today - datetime.timedelta(days=today.weekday()-4)
   return lastmonday

@property
def monday_is_past(self):
   print("fecha   lll l "+self)
   lastmonday = self.date - datetime.timedelta(days=self.date.weekday())
   return datetime.datetime.today() > self.date