# Python3 - Django : Issues and Resolutions

### Issue 1:
<b>Issue:</b>
<p>django.template.exceptions.TemplateSyntaxError: 'static' is not a registered tag library. Must be one of:
<p>
<b>Resolution:</b>
<p>Issue get resolved ,What I did I added static library in options following is code
```django
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
This worked for me
```
