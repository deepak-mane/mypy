# Python3 - Django : Issues and Resolutions

1.) <b>Issue:</b>django.template.exceptions.TemplateSyntaxError: 'static' is not a registered tag library. Must be one of:
<b>Resolution:</b>Issue get resolved ,What I did I added static library in options following is code,This worked for me:
        
```python
'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
        'libraries': { # Adding this section should work around the issue.
            'staticfiles' : 'django.templatetags.static',
        },
    }, 

```
### Issue 2:
<b>Issue:</b> <p>OperationalError: database is locked
<p>
<b>Resolution:</b>
<p>It was because I open the database from SQLite Browser. When I close it from the browser, the problem is gone
