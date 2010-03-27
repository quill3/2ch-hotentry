#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Sites(db.Model):
  url = db.StringProperty()
  title = db.StringProperty()
  check_time = db.DateTimeProperty()

class Entries(db.Model):
  url = db.StringProperty()
  title = db.StringProperty(multiline=True)
  date = db.StringProperty()
  count = db.IntegerProperty()
  increase1 = db.IntegerProperty()
  increase2 = db.IntegerProperty()
  increase3 = db.IntegerProperty()  
  score = db.IntegerProperty()
  parent_site = db.ReferenceProperty(Sites)