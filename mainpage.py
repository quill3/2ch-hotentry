#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datastores

query = datastores.Entries.gql('ORDER BY score DESC')
fetched_entries = query.fetch(30)

print '''<html>
<head>
<title>2ch Matome Hot Entry</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<link rel="stylesheet" type="text/css" href="css/html.css" />
<link rel="stylesheet" type="text/css" href="css/layout.css" />
</head>
<body>
<div id="wrapper">
<div id="content">
<div id="header">
<h1>2ch Matome Hot Entry</h1>
<h2><span class="highlight">２ちゃんねるまとめサイトだけでホットエントリー</span></h2>
</div>
<div id="page">'''


for fetched_entry in fetched_entries:
  print '<span class="result"><a href="' + fetched_entry.url.encode('utf-8')  + '" target="_blank" >' + fetched_entry.title.encode('utf-8') +'</a></span>'
  print '<br>'
  print '<span class="users"><strong><a href="http://b.hatena.ne.jp/entry/' + fetched_entry.url.encode('utf-8') + '" target="_blank">' + str(fetched_entry.count) + ' users</a></strong></span>&nbsp;&nbsp;'
  print '<span class="timestamp">' + fetched_entry.date.encode('utf-8') + '</span>'
  #print '<br>'
  #print 'score:' + str(fetched_entry.score) + '  (' + str(fetched_entry.increase1) + '/' + str(fetched_entry.increase2) + '/' + str(fetched_entry.increase3) + ')'
  print '<br><br>'

print '''<div class="footer">
<img src="http://code.google.com/appengine/images/appengine-noborder-120x30.gif" alt="Powered by Google App Engine" />
<br>
This service is created by <a href="http://d.hatena.ne.jp/quill3/" target="_blank" >quill3</a>.
<br>
(Here is <a href="http://github.com/quill3/2ch-hotentry" target="_blank" >source code</a> & <a href="http://d.hatena.ne.jp/quill3/archive?word=%2A%5B2ch%A4%DE%A4%C8%A4%E1hotentry%5D" target="_blank" >development log</a>.)
</div>

</div>
</div>
</div>

<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-568420-6");
pageTracker._trackPageview();
} catch(err) {}</script>

</body>
</html>'''