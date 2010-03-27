#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.api import urlfetch
import re
import datetime

import datastores

query1 = datastores.Sites.gql('ORDER BY check_time ASC')
site = query1.get()

if site:
  entrylist_url = 'http://b.hatena.ne.jp/entrylist?url=' + site.url
  result = urlfetch.fetch(entrylist_url)
  if result.status_code == 200:
##score clear
    query2 = datastores.Entries.gql('WHERE parent_site = :parent_site AND score > :score',parent_site=site,score=0)
    for scorefilled_entry in query2:
      scorefilled_entry.score = 0
      scorefilled_entry.put()
##data add
    #print result.content
    pattern = re.compile(r'''<li class="users"> <strong><a href="/entry/(.*?)" title="(.*?)">(.*?) users</a></strong></li>
        <li class="timestamp">(.*?)</li>(.*?)
        <cite title="(.*?)"><a href="(.*?)"> 続きを読む</a></cite>''',re.S)
    entry_lists = pattern.findall(result.content)
    for entry_list in entry_lists:
      #print entry_list[6]
      #print entry_list[5]
      #print entry_list[3]
      #print entry_list[2]
      #print '<br>'
      query3 = datastores.Entries.gql('WHERE url = :url',url=entry_list[6])
      entry = query3.get()
      if entry:
        entry.increase3 = entry.increase2
        entry.increase2 = entry.increase1
        entry.increase1 = int(entry_list[2]) - entry.count
        entry.count = int(entry_list[2])
      else:
        entry = datastores.Entries()
        entry.url = entry_list[6]
        entry.title = unicode(entry_list[5],'utf-8')
        entry.date = entry_list[3]
        entry.count = int(entry_list[2])
        entry.increase3 = 0
        entry.increase2 = 0
        entry.increase1 = int(entry_list[2])
        entry.parent_site = site
      entry.score = entry.increase1 + int(entry.increase2 * 0.6) + int(entry.increase3 * 0.3)
      entry.put()
    site.check_time = datetime.datetime.today()
    site.put()