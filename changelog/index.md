---
layout: default
title: Flacon - Changelog
menuItem: download
---

## ChangeLog
<br>

{% for post in site.categories.changelog limit 5 %}
<h3>{{post.title}} <i style="font-weight: normal; font-size: 90%;">({{ post.date | date_to_string}})</i></h3>
{{ post.content }}
<br>
{% endfor %}
