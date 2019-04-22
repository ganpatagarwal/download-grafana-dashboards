# Download Grafana Dashboards
Many times we want to save a list of grafana dashboards on our local machine
to either create a backup or buk share.

It is a time taking and boring task to go through them one by one and
click a set of links to download.

Came up with this small program which uses python3 + selenium webdriver + chromedriver
to make things easy.

**PS: I have tested this program on MacOS only**

## Things to install on MAC

### Grafana Server (V5.1 or above)
Obviously, Yes

### Chrome Browser
You know how to do that :-)

### Chromedriver
```brew tap homebrew/cask && brew cask install chromedriver```

### Selenium
```pip3 install selenium```

## Steps to execute

### List your dashboards
Add all your dashboard links to `dashboard_links.txt` file

### Run program
```
python3 download.py
```

## What it does
- Creates a local current timestamped folder.

- Iterates through the links.

- Downloads `.json` file inside folder

## Anything else is needed?
Feel free to customize and re-use
