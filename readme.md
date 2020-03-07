#Starkeeper

Starkeeper is designed for starring (unstaring) the repositories of those people who star(unstar) your repositories.

##Configuration

~~~
GITHUB_TOKEN = 'Paste your Github API Token here'
NUMBER = 10 # The number of randomly selected repos which will be starred.
~~~

##Setup

Github tokens can be obtained from [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line).

Any online service, which supports Flask backend can be used for setting up starkeeper. https://pythonanywhere.com has been verified.

Starkeeper is a web hook listener which works upon **json** data for indentifying star and unstar events. Therefore, for each repository for which you want to enable starkeeper, you need to setup the webhook settings, instructions can be found [here](https://developer.github.com/webhooks/):

Make sure you setup the content type as Application/json.

##Steps

1. Setup an account on https://pythonanywhere.com. Setup a webapp using Flask and add the contents of the starkeeper to the webapp file.
2. Issue Github API Token for your account from [here](https://github.com/settings/tokens), and add it to GITHUB_TOKEN field.
3. For enabling starkeeper for the repository do the following:
    1. Go to settings and enable webhooks.
    2. In the webhook url, paste the hyperlink which you got in the first step.
    3. In the webhook triggers, select 'stars'.
    4. In the content type select application/json.
